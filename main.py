from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField
from passlib.hash import sha256_crypt
from functools import wraps
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments import highlight


LEXERS = sorted(get_all_lexers(), key=lambda l: l[0].lower())

app = Flask(__name__)

# Config MYSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'spqr'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init MYSQL
mysql = MySQL(app)


@app.route("/")
def index():
    return render_template('index.html')


# Trending
@app.route('/public_paste')
def public_paste():
    cur = mysql.connection.cursor()

    result = cur.execute("SELECT * FROM paste")
    paste = cur.fetchall()

    if result > 0:
        return render_template('public_paste.html', paste=paste)
    else:
        msg = 'No Artciles Found'
        return render_template('public_paste.html', msg=msg)
    cur.close()


# Single Paste
@app.route('/public_paste/<string:id>/')
def single_paste(id):
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM paste WHERE id=%s", [id])

    paste = cur.fetchone()
    raw_code = paste['body']
    programming_language = get_lexer_by_name(paste['syntax'])

    highlighted_code = highlight(raw_code, programming_language, HtmlFormatter())

    return render_template('single_paste.html', paste=paste, highlighted_code=highlighted_code)


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [validators.DataRequired(),
                                          validators.EqualTo('confirm', message='Passwords do not match')])
    confirm = PasswordField('Confirm Password')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # create cursor
        cur =  mysql.connection.cursor()

        cur.execute("INSERT INTO users(name,email,username,password) VALUES (%s,%s,%s,%s)", (name, email, username, password))

        # commit
        mysql.connection.commit()

        # close
        cur.close()

        flash('You are now registered and can log in', 'successful')
        redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        passwordcandidate = request.form['password']

        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM users WHERE username =%s", [username])

        if result > 0:
            data = cur.fetchone()
            password = data['password']

            if sha256_crypt.verify(passwordcandidate, password):
                session['logged_in'] = True
                session['username'] = username

                flash('You are now login', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized please login', 'danger')
            return redirect(url_for('login'))
    return wrap


@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


@app.route('/dashboard')
@is_logged_in
def dashboard():

    cur = mysql.connection.cursor()

    result = cur.execute("SELECT * FROM paste")
    paste = cur.fetchall()

    if result > 0:
        return render_template('dashboard.html', paste=paste)
    else:
        msg = 'No Artciles Found'
        return render_template('dashboard.html', msg=msg)
    cur.close()


class AccountForm(Form):
    password = StringField('Password', [validators.Length(min=6)])


@app.route('/settings/<string:username>/', methods=['GET', 'POST'])
@is_logged_in
def settings(username):

    cur = mysql.connection.cursor()

    result = cur.execute("SELECT * FROM users WHERE username =%s", [username])

    paste = cur.fetchone()

    form = AccountForm(request.form)
    form.password.data = paste['password']

    if request.method == 'POST' and form.validate():
        password = request.form['password']

        cur = mysql.connection.cursor()

        cur.execute("UPDATE users SET password=%s WHERE username=%s",
                    (password, username))

        mysql.connection.commit()
        cur.close()

        flash('Paste Updated', 'success')

        return redirect(url_for('dashboard'))

    return render_template('settings.html', form=form)

lexers = LEXERS

for lexer in lexers:
    print ("('" +(lexer[1][0]) + "'),('"+(lexer[0])+"')")


# New Paste Form
class PasteForm(Form):
    body = TextAreaField('New Paste', [validators.Length(min=1)])
    # u'Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')]
    # 'Syntax Highlighting:', [validators.Length(min=1)]

    syntax = SelectField(u'Programming Language', choices=[('text', 'Text only'),('abap', 'ABAP'),
('abnf', 'ABNF'),
('as', 'ActionScript'),
('as3', 'ActionScript 3'),
('ada', 'Ada'),
('adl', 'ADL'),
('agda', 'Agda'),
('aheui', 'Aheui'),
('alloy', 'Alloy'),
('at', 'AmbientTalk'),
('ampl', 'Ampl'),
('ng2', 'Angular2'),
('antlr', 'ANTLR'),
('antlr-as', 'ANTLR With ActionScript Target'),
('antlr-csharp', 'ANTLR With C# Target'),
('antlr-cpp', 'ANTLR With CPP Target'),
('antlr-java', 'ANTLR With Java Target'),
('antlr-objc', 'ANTLR With ObjectiveC Target'),
('antlr-perl', 'ANTLR With Perl Target'),
('antlr-python', 'ANTLR With Python Target'),
('antlr-ruby', 'ANTLR With Ruby Target'),
('apacheconf', 'ApacheConf'),
('apl', 'APL'),
('applescript', 'AppleScript'),
('arduino', 'Arduino'),
('aspectj', 'AspectJ'),
('aspx-cs', 'aspx-cs'),
('aspx-vb', 'aspx-vb'),
('asy', 'Asymptote'),
('ahk', 'autohotkey'),
('autoit', 'AutoIt'),
('awk', 'Awk'),
('basemake', 'Base Makefile'),
('bash', 'Bash'),
('console', 'Bash Session'),
('bat', 'Batchfile'),
('bbcode', 'BBCode'),
('bc', 'BC'),
('befunge', 'Befunge'),
('bib', 'BibTeX'),
('blitzbasic', 'BlitzBasic'),
('blitzmax', 'BlitzMax'),
('bnf', 'BNF'),
('boo', 'Boo'),
('boogie', 'Boogie'),
('brainfuck', 'Brainfuck'),
('bro', 'Bro'),
('bst', 'BST'),
('bugs', 'BUGS'),
('c', 'C'),
('csharp', 'C#'),
('cpp', 'C++'),
('c-objdump', 'c-objdump'),
('ca65', 'ca65 assembler'),
('cadl', 'cADL'),
('camkes', 'CAmkES'),
('capnp', "Cap'n Proto"),
('capdl', 'CapDL'),
('cbmbas', 'CBM BASIC V2'),
('ceylon', 'Ceylon'),
('cfengine3', 'CFEngine3'),
('cfs', 'cfstatement'),
('chai', 'ChaiScript'),
('chapel', 'Chapel'),
('cheetah', 'Cheetah'),
('cirru', 'Cirru'),
('clay', 'Clay'),
('clean', 'Clean'),
('clojure', 'Clojure'),
('clojurescript', 'ClojureScript'),
('cmake', 'CMake'),
('cobol', 'COBOL'),
('cobolfree', 'COBOLFree'),
('coffee-script', 'CoffeeScript'),
('cfc', 'Coldfusion CFC'),
('cfm', 'Coldfusion HTML'),
('common-lisp', 'Common Lisp'),
('componentpascal', 'Component Pascal'),
('coq', 'Coq'),
('cpp-objdump', 'cpp-objdump'),
('cpsa', 'CPSA'),
('crmsh', 'Crmsh'),
('croc', 'Croc'),
('cryptol', 'Cryptol'),
('cr', 'Crystal'),
('csound-document', 'Csound Document'),
('csound', 'Csound Orchestra'),
('csound-score', 'Csound Score'),
('css', 'CSS'),
('css+django', 'CSS+Django/Jinja'),
('css+genshitext', 'CSS+Genshi Text'),
('css+lasso', 'CSS+Lasso'),
('css+mako', 'CSS+Mako'),
('css+mozpreproc', 'CSS+mozpreproc'),
('css+myghty', 'CSS+Myghty'),
('css+php', 'CSS+PHP'),
('css+erb', 'CSS+Ruby'),
('css+smarty', 'CSS+Smarty'),
('cuda', 'CUDA'),
('cypher', 'Cypher'),
('cython', 'Cython'),
('d', 'D'),
('d-objdump', 'd-objdump'),
('dpatch', 'Darcs Patch'),
('dart', 'Dart'),
('control', 'Debian Control file'),
('sourceslist', 'Debian Sourcelist'),
('delphi', 'Delphi'),
('dg', 'dg'),
('diff', 'Diff'),
('django', 'Django/Jinja'),
('docker', 'Docker'),
('dtd', 'DTD'),
('duel', 'Duel'),
('dylan', 'Dylan'),
('dylan-console', 'Dylan session'),
('dylan-lid', 'DylanLID'),
('earl-grey', 'Earl Grey'),
('easytrieve', 'Easytrieve'),
('ebnf', 'EBNF'),
('ec', 'eC'),
('ecl', 'ECL'),
('eiffel', 'Eiffel'),
('elixir', 'Elixir'),
('iex', 'Elixir iex session'),
('elm', 'Elm'),
('emacs', 'EmacsLisp'),
('ragel-em', 'Embedded Ragel'),
('erb', 'ERB'),
('erlang', 'Erlang'),
('erl', 'Erlang erl session'),
('evoque', 'Evoque'),
('ezhil', 'Ezhil'),
('factor', 'Factor'),
('fancy', 'Fancy'),
('fan', 'Fantom'),
('felix', 'Felix'),
('fish', 'Fish'),
('flatline', 'Flatline'),
('forth', 'Forth'),
('fortran', 'Fortran'),
('fortranfixed', 'FortranFixed'),
('foxpro', 'FoxPro'),
('fsharp', 'FSharp'),
('gap', 'GAP'),
('gas', 'GAS'),
('genshi', 'Genshi'),
('genshitext', 'Genshi Text'),
('pot', 'Gettext Catalog'),
('cucumber', 'Gherkin'),
('glsl', 'GLSL'),
('gnuplot', 'Gnuplot'),
('go', 'Go'),
('golo', 'Golo'),
('gooddata-cl', 'GoodData-CL'),
('gosu', 'Gosu'),
('gst', 'Gosu Template'),
('groff', 'Groff'),
('groovy', 'Groovy'),
('haml', 'Haml'),
('handlebars', 'Handlebars'),
('haskell', 'Haskell'),
('hx', 'Haxe'),
('hexdump', 'Hexdump'),
('hsail', 'HSAIL'),
('html', 'HTML'),
('html+ng2', 'HTML + Angular2'),
('html+cheetah', 'HTML+Cheetah'),
('html+django', 'HTML+Django/Jinja'),
('html+evoque', 'HTML+Evoque'),
('html+genshi', 'HTML+Genshi'),
('html+handlebars', 'HTML+Handlebars'),
('html+lasso', 'HTML+Lasso'),
('html+mako', 'HTML+Mako'),
('html+myghty', 'HTML+Myghty'),
('html+php', 'HTML+PHP'),
('html+smarty', 'HTML+Smarty'),
('html+twig', 'HTML+Twig'),
('html+velocity', 'HTML+Velocity'),
('http', 'HTTP'),
('haxeml', 'Hxml'),
('hylang', 'Hy'),
('hybris', 'Hybris'),
('idl', 'IDL'),
('idris', 'Idris'),
('igor', 'Igor'),
('inform6', 'Inform 6'),
('i6t', 'Inform 6 template'),
('inform7', 'Inform 7'),
('ini', 'INI'),
('io', 'Io'),
('ioke', 'Ioke'),
('irc', 'IRC logs'),
('isabelle', 'Isabelle'),
('j', 'J'),
('jags', 'JAGS'),
('jasmin', 'Jasmin'),
('java', 'Java'),
('jsp', 'Java Server Page'),
('js', 'JavaScript'),
('js+cheetah', 'JavaScript+Cheetah'),
('js+django', 'JavaScript+Django/Jinja'),
('js+genshitext', 'JavaScript+Genshi Text'),
('js+lasso', 'JavaScript+Lasso'),
('js+mako', 'JavaScript+Mako'),
('javascript+mozpreproc', 'Javascript+mozpreproc'),
('js+myghty', 'JavaScript+Myghty'),
('js+php', 'JavaScript+PHP'),
('js+erb', 'JavaScript+Ruby'),
('js+smarty', 'JavaScript+Smarty'),
('jcl', 'JCL'),
('jsgf', 'JSGF'),
('json', 'JSON'),
('jsonld', 'JSON-LD'),
('json-object', 'JSONBareObject'),
('julia', 'Julia'),
('jlcon', 'Julia console'),
('juttle', 'Juttle'),
('kal', 'Kal'),
('kconfig', 'Kconfig'),
('koka', 'Koka'),
('kotlin', 'Kotlin'),
('lasso', 'Lasso'),
('lean', 'Lean'),
('less', 'LessCss'),
('lighty', 'Lighttpd configuration file'),
('limbo', 'Limbo'),
('liquid', 'liquid'),
('lagda', 'Literate Agda'),
('lcry', 'Literate Cryptol'),
('lhs', 'Literate Haskell'),
('lidr', 'Literate Idris'),
('live-script', 'LiveScript'),
('llvm', 'LLVM'),
('logos', 'Logos'),
('logtalk', 'Logtalk'),
('lsl', 'LSL'),
('lua', 'Lua'),
('make', 'Makefile'),
('mako', 'Mako'),
('maql', 'MAQL'),
('md', 'markdown'),
('mask', 'Mask'),
('mason', 'Mason'),
('mathematica', 'Mathematica'),
('matlab', 'Matlab'),
('matlabsession', 'Matlab session'),
('minid', 'MiniD'),
('modelica', 'Modelica'),
('modula2', 'Modula-2'),
('trac-wiki', 'MoinMoin/Trac Wiki markup'),
('monkey', 'Monkey'),
('monte', 'Monte'),
('moocode', 'MOOCode'),
('moon', 'MoonScript'),
('mozhashpreproc', 'mozhashpreproc'),
('mozpercentpreproc', 'mozpercentpreproc'),
('mql', 'MQL'),
('mscgen', 'Mscgen'),
('doscon', 'MSDOS Session'),
('mupad', 'MuPAD'),
('mxml', 'MXML'),
('myghty', 'Myghty'),
('mysql', 'MySQL'),
('nasm', 'NASM'),
('ncl', 'NCL'),
('nemerle', 'Nemerle'),
('nesc', 'nesC'),
('newlisp', 'NewLisp'),
('newspeak', 'Newspeak'),
('nginx', 'Nginx configuration file'),
('nim', 'Nimrod'),
('nit', 'Nit'),
('nixos', 'Nix'),
('nsis', 'NSIS'),
('numpy', 'NumPy'),
('nusmv', 'NuSMV'),
('objdump', 'objdump'),
('objdump-nasm', 'objdump-nasm'),
('objective-c', 'Objective-C'),
('objective-c++', 'Objective-C++'),
('objective-j', 'Objective-J'),
('ocaml', 'OCaml'),
('octave', 'Octave'),
('odin', 'ODIN'),
('ooc', 'Ooc'),
('opa', 'Opa'),
('openedge', 'OpenEdge ABL'),
('pacmanconf', 'PacmanConf'),
('pan', 'Pan'),
('parasail', 'ParaSail'),
('pawn', 'Pawn'),
('perl', 'Perl'),
('perl6', 'Perl6'),
('php', 'PHP'),
('pig', 'Pig'),
('pike', 'Pike'),
('pkgconfig', 'PkgConfig'),
('plpgsql', 'PL/pgSQL'),
('psql', 'PostgreSQL console (psql)'),
('postgresql', 'PostgreSQL SQL dialect'),
('postscript', 'PostScript'),
('pov', 'POVRay'),
('powershell', 'PowerShell'),
('ps1con', 'PowerShell Session'),
('praat', 'Praat'),
('prolog', 'Prolog'),
('properties', 'Properties'),
('protobuf', 'Protocol Buffer'),
('pug', 'Pug'),
('puppet', 'Puppet'),
('pypylog', 'PyPy Log'),
('python', 'Python'),
('python3', 'Python 3'),
('py3tb', 'Python 3.0 Traceback'),
('pycon', 'Python console session'),
('pytb', 'Python Traceback'),
('qbasic', 'QBasic'),
('qml', 'QML'),
('qvto', 'QVTO'),
('racket', 'Racket'),
('ragel', 'Ragel'),
('ragel-c', 'Ragel in C Host'),
('ragel-cpp', 'Ragel in CPP Host'),
('ragel-d', 'Ragel in D Host'),
('ragel-java', 'Ragel in Java Host'),
('ragel-objc', 'Ragel in Objective C Host'),
('ragel-ruby', 'Ragel in Ruby Host'),
('raw', 'Raw token data'),
('rconsole', 'RConsole'),
('rd', 'Rd'),
('rebol', 'REBOL'),
('red', 'Red'),
('redcode', 'Redcode'),
('registry', 'reg'),
('rnc', 'Relax-NG Compact'),
('resource', 'ResourceBundle'),
('rst', 'reStructuredText'),
('rexx', 'Rexx'),
('rhtml', 'RHTML'),
('roboconf-graph', 'Roboconf Graph'),
('roboconf-instances', 'Roboconf Instances'),
('robotframework', 'RobotFramework'),
('spec', 'RPMSpec'),
('rql', 'RQL'),
('rsl', 'RSL'),
('rb', 'Ruby'),
('rbcon', 'Ruby irb session'),
('rust', 'Rust'),
('splus', 'S'),
('sas', 'SAS'),
('sass', 'Sass'),
('scala', 'Scala'),
('ssp', 'Scalate Server Page'),
('scaml', 'Scaml'),
('scheme', 'Scheme'),
('scilab', 'Scilab'),
('scss', 'SCSS'),
('shen', 'Shen'),
('silver', 'Silver'),
('slim', 'Slim'),
('smali', 'Smali'),
('smalltalk', 'Smalltalk'),
('smarty', 'Smarty'),
('snobol', 'Snobol'),
('snowball', 'Snowball'),
('sp', 'SourcePawn'),
('sparql', 'SPARQL'),
('sql', 'SQL'),
('sqlite3', 'sqlite3con'),
('squidconf', 'SquidConf'),
('stan', 'Stan'),
('sml', 'Standard ML'),
('stata', 'Stata'),
('sc', 'SuperCollider'),
('swift', 'Swift'),
('swig', 'SWIG'),
('systemverilog', 'systemverilog'),
('tads3', 'TADS 3'),
('tap', 'TAP'),
('tasm', 'TASM'),
('tcl', 'Tcl'),
('tcsh', 'Tcsh'),
('tcshcon', 'Tcsh Session'),
('tea', 'Tea'),
('termcap', 'Termcap'),
('terminfo', 'Terminfo'),
('terraform', 'Terraform'),
('tex', 'TeX'),
('text', 'Text only'),
('thrift', 'Thrift'),
('todotxt', 'Todotxt'),
('rts', 'TrafficScript'),
('tsql', 'Transact-SQL'),
('treetop', 'Treetop'),
('turtle', 'Turtle'),
('twig', 'Twig'),
('ts', 'TypeScript'),
('typoscript', 'TypoScript'),
('typoscriptcssdata', 'TypoScriptCssData'),
('typoscripthtmldata', 'TypoScriptHtmlData'),
('urbiscript', 'UrbiScript'),
('vala', 'Vala'),
('vb.net', 'VB.net'),
('vcl', 'VCL'),
('vclsnippets', 'VCLSnippets'),
('vctreestatus', 'VCTreeStatus'),
('velocity', 'Velocity'),
('verilog', 'verilog'),
('vgl', 'VGL'),
('vhdl', 'vhdl'),
('vim', 'VimL'),
('wdiff', 'WDiff'),
('whiley', 'Whiley'),
('x10', 'X10'),
('xml', 'XML'),
('xml+cheetah', 'XML+Cheetah'),
('xml+django', 'XML+Django/Jinja'),
('xml+evoque', 'XML+Evoque'),
('xml+lasso', 'XML+Lasso'),
('xml+mako', 'XML+Mako'),
('xml+myghty', 'XML+Myghty'),
('xml+php', 'XML+PHP'),
('xml+erb', 'XML+Ruby'),
('xml+smarty', 'XML+Smarty'),
('xml+velocity', 'XML+Velocity'),
('xquery', 'XQuery'),
('xslt', 'XSLT'),
('xtend', 'Xtend'),
('extempore', 'xtlang'),
('xul+mozpreproc', 'XUL+mozpreproc'),
('yaml', 'YAML'),
('yaml+jinja', 'YAML+Jinja'),
('zephir', 'Zephir')])


    expire = SelectField('Paste Expiration:', choices=[('Never', 'Never')])
    exposure = SelectField(u'Exposure', choices=[('public', 'Public'), ('private', 'Private')])
    title = StringField('Title', [validators.Length(min=1, max=200)])


@app.route('/new_paste', methods=['GET', 'POST'])
def new_paste():
    form = PasteForm(request.form)
    if request.method == 'POST' and form.validate():
        body = form.body.data
        syntax = form.syntax.data
        expire = form.expire.data
        exposure = form.exposure.data
        title = form.title.data

        cur = mysql.connection.cursor()

        if is_logged_in == True:
            cur.execute("INSERT INTO paste(body,syntax,expiration,exposure,title,author) VALUES (%s,%s,%s,%s,%s,%s)",
                    (body, syntax, expire, exposure, title, session['username']))
        else:
            session['username'] = 'Guest'
            cur.execute("INSERT INTO paste(body,syntax,expiration,exposure,title,author) VALUES (%s,%s,%s,%s,%s,%s)",
                        (body, syntax, expire, exposure, title, session['username']))

        mysql.connection.commit()
        cur.close()

        flash('Paste Created', 'success')
        if is_logged_in == True:
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('public_paste'))

    return render_template('new_paste.html',lexer=LEXERS, form=form)


# Edit Paste
@app.route('/edit_paste/<string:id>/', methods=['GET', 'POST'])
@is_logged_in
def edit_paste(id):
    cur = mysql.connection.cursor()

    # get id from paste
    result = cur.execute("SELECT * FROM paste WHERE id=%s", [id])

    paste = cur.fetchone()

    #Get form
    form = PasteForm(request.form)
    form.body.data = paste['body']
    form.syntax.data = paste['syntax']
    form.expire.data = paste['expiration']
    form.exposure.data = paste['exposure']
    form.title.data = paste['title']

    if request.method == 'POST' and form.validate():
        body = request.form['body']
        syntax = request.form['syntax']
        expire = request.form['expire']
        exposure = request.form['exposure']
        title = request.form['title']

        cur = mysql.connection.cursor()


        cur.execute("UPDATE paste SET body=%s, syntax=%s, expiration=%s, exposure=%s, title=%s WHERE id=%s",
                    (body,syntax,expire,exposure,title,id))

        mysql.connection.commit()
        cur.close()

        flash('Paste Updated', 'success')

        return redirect(url_for('dashboard'))

    return render_template('edit_paste.html', form=form)


@app.route('/delete_paste/<string:id>/', methods=['POST'])
@is_logged_in
def delete_paste(id):

    cur = mysql.connection.cursor()

    cur.execute("DELETE FROM paste WHERE id=%s", [id])

    mysql.connection.commit()
    cur.close()

    flash('Paste Deleted', 'success')

    return redirect(url_for('my_paste'))



@app.route('/my_paste')
@is_logged_in
def my_paste():
    cur = mysql.connection.cursor()

    result = cur.execute("SELECT * FROM paste WHERE author=%s", [session['username']])
    paste = cur.fetchall()

    if result > 0:
        return render_template('my_paste.html', paste=paste)
    else:
        msg = 'No Artciles Found'
        return render_template('my_paste.html', msg=msg)
    cur.close()


if __name__ == '__main__':
    app.secret_key='hooray12345'
    app.run(debug=True)
