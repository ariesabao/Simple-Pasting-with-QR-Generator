-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 22, 2018 at 11:37 AM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.2.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `spqr`
--

-- --------------------------------------------------------

--
-- Table structure for table `paste`
--

CREATE TABLE `paste` (
  `id` int(11) NOT NULL,
  `body` text,
  `syntax` varchar(100) DEFAULT NULL,
  `expiration` varchar(100) DEFAULT NULL,
  `exposure` varchar(50) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `create_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `paste`
--

INSERT INTO `paste` (`id`, `body`, `syntax`, `expiration`, `exposure`, `title`, `author`, `create_date`) VALUES
(8, '<p>Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, and a syntax that allows programmers to express concepts in fewer lines of code,[25][26] notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.[27]</p><p>Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.[28]</p><p>Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software[29] and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation.</p>', 'Python', 'Never', 'Public', 'Python ( wikipedia ) ', 'aries', '2018-02-07 04:43:13'),
(9, '<p>Unlike a Cookie,&nbsp;<strong>Session</strong>&nbsp;data is stored on server. Session is the time interval when a client logs into a server and logs out of it. The data, which is needed to be held across this session, is stored in a temporary directory on the server.</p><p>A session with each client is assigned a&nbsp;<strong>Session ID</strong>. The Session data is stored on top of cookies and the server signs them cryptographically. For this encryption, a Flask application needs a defined&nbsp;<strong>SECRET_KEY</strong>.</p><p>Session object is also a dictionary object containing key-value pairs of session variables and associated values.</p><p>For example, to set a&nbsp;<strong>&lsquo;username&rsquo;</strong>&nbsp;session variable use the statement &minus;</p>', 'Python', 'Never', 'Public', 'Flask – Sessions', 'aries', '2018-02-07 04:48:13'),
(10, '<p>wew</p>', 'wew', 'wew', 'wew', 'wew guest', 'Guest', '2018-02-07 04:54:58'),
(11, '<p>guest&nbsp;guest&nbsp;guest&nbsp;guest&nbsp;guest&nbsp;</p>', 'guest ', 'guest ', 'guest ', 'guest ', 'Guest', '2018-02-07 04:57:55'),
(12, 'print(\"Programming is fun!\")', 'Python', 'Never', 'public', 'Python Test', 'Guest', '2018-02-09 00:43:43'),
(13, '<p># Single Paste @app.route(&#39;/public_paste/&lt;string:id&gt;/&#39;) def single_paste(id): cur = mysql.connection.cursor() result = cur.execute(&quot;SELECT * FROM paste WHERE id=%s&quot;, [id]) paste = cur.fetchone() programming_language = get_lexer_by_name(paste[&#39;syntax&#39;]) raw_code = str(paste[&#39;body&#39;]) highlighted_code = highlight(raw_code, programming_language, HtmlFormatter()) return render_template(&#39;single_paste.html&#39;,highlighted_code=highlighted_code, paste=paste)</p>', 'Python', 'Never', 'public', 'Single_paste', 'Guest', '2018-02-09 01:00:09'),
(14, '<p>wew</p>', 'zephir', 'Never', 'public', 'wew', 'Guest', '2018-02-09 01:22:37'),
(15, '# Trending\r\n@app.route(\'/public_paste\')\r\ndef public_paste():\r\n    cur = mysql.connection.cursor()\r\n\r\n    result = cur.execute(\"SELECT * FROM paste\")\r\n    paste = cur.fetchall()\r\n\r\n    if result > 0:\r\n        return render_template(\'public_paste.html\', paste=paste)\r\n    else:\r\n        msg = \'No Artciles Found\'\r\n        return render_template(\'public_paste.html\', msg=msg)\r\n    cur.close()', 'python', 'Never', 'public', 'public_paste', 'Guest', '2018-02-11 14:43:44'),
(16, '# New Paste Form\r\nclass PasteForm(Form):\r\n    body = TextAreaField(\'New Paste\', [validators.Length(min=1, max=1000)])\r\n    # u\'Programming Language\', choices=[(\'cpp\', \'C++\'), (\'py\', \'Python\'), (\'text\', \'Plain Text\')]\r\n    # \'Syntax Highlighting:\', [validators.Length(min=1)]\r\n    for lexer in lexers:\r\n        syntax = SelectField(u\'Programming Language\', choices=[(\'py\', \'Python\')])\r\n\r\n    expire = SelectField(\'Paste Expiration:\', choices=[(\'Never\', \'Never\')])\r\n    exposure = SelectField(u\'Exposure\', choices=[(\'public\', \'Public\'), (\'private\', \'Private\')])\r\n    title = StringField(\'Title\', [validators.Length(min=1, max=200)])', 'py', 'Never', 'public', 'class PasteForm(Form):', 'Guest', '2018-02-11 16:13:54'),
(17, '<p>#test html strip tags</p>', 'py', 'Never', 'public', 'test html strip tags', 'Guest', '2018-02-11 16:32:38'),
(18, '<p>#How to install PYTHON 3.6.4</p>', 'py', 'Never', 'public', 'How to install PYTHON 3.6.4', 'Guest', '2018-02-11 16:33:51'),
(19, '<p>if __name__ == &#39;__main__&#39;:<br />&nbsp; &nbsp; app.secret_key=&#39;hooray12345&#39;<br />&nbsp; &nbsp; app.run(debug=True)</p>', 'py', 'Never', 'public', 'if __name__', 'Guest', '2018-02-11 16:40:23'),
(20, 'from flask import Flask, render_template, flash, redirect, url_for, session, logging, request\r\nfrom flask_mysqldb import MySQL\r\nfrom wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField\r\nfrom passlib.hash import sha256_crypt\r\nfrom functools import wraps\r\nfrom pygments.lexers import get_all_lexers, get_lexer_by_name\r\nfrom pygments.formatters import HtmlFormatter\r\nfrom pygments import highlight', 'py', 'Never', 'public', 'import', 'Guest', '2018-02-11 16:49:54'),
(21, '<p>wew</p>', 'py', 'Never', 'public', 'w', 'Guest', '2018-02-11 17:13:30'),
(22, '<p>ngee</p>', 'py', 'Never', 'public', 'ngekkk', 'Guest', '2018-02-11 18:16:29'),
(23, '@app.route(\"/\")\r\ndef index():\r\n    return render_template(\'index.html\')', 'py', 'Never', 'public', 'index', 'Guest', '2018-02-11 18:23:49'),
(24, '<p>config.forcePasteAsPlainText = true;</p>', 'py', 'Never', 'public', 'config.forcePasteAsPlainText = true;', 'Guest', '2018-02-11 18:26:40'),
(25, '  #include \'std_lib_facilities.h\'\r\n\r\nint main()\r\n{\r\n	cout << \'Hello World!\\n\';\r\n	return 0;\r\n}', 'cpp', 'Never', 'public', 'c++', 'Guest', '2018-02-11 19:02:19'),
(26, 'function getPlainText( strSrc ) {\r\n	var resultStr = \"\";\r\n    \r\n    // Ignore the <p> tag if it is in very start of the text\r\n    if(strSrc.indexOf(\'<p>\') == 0)\r\n        resultStr = strSrc.substring(3);\r\n    \r\n	// Replace <p> with two newlines\r\n    resultStr = resultStr.replace(/<p>/gi, \"\\r\\n\\r\\n\");\r\n	// Replace <br /> with one newline\r\n    resultStr = resultStr.replace(/<br \\/>/gi, \"\\r\\n\");\r\n    resultStr = resultStr.replace(/<br>/gi, \"\\r\\n\");\r\n	\r\n	//-+-+-+-+-+-+-+-+-+-+-+\r\n	// Strip off other HTML tags.\r\n	//-+-+-+-+-+-+-+-+-+-+-+\r\n	\r\n	return  resultStr.replace( /<[^<|>]+?>/gi,\'\' );\r\n}', 'js', 'Never', 'public', 'Javascript', 'Guest', '2018-02-11 19:05:16'),
(27, 'for lexer in lexers:\r\n    print (\"(\'\" +(lexer[1][0]) + \"\'),(\'\"+(lexer[0])+\"\')\")', 'python3', 'Never', 'public', 'lexer', 'Guest', '2018-02-11 19:24:08'),
(28, '/******************************************************************************\r\n *  Compilation:  javac HelloWorld.java\r\n *  Execution:    java HelloWorld\r\n *\r\n *  Prints \"Hello, World\". By tradition, this is everyone\'s first program.\r\n *\r\n *  % java HelloWorld\r\n *  Hello, World\r\n *\r\n *  These 17 lines of text are comments. They are not part of the program;\r\n *  they serve to remind us about its properties. The first two lines tell\r\n *  us what to type to compile and test the program. The next line describes\r\n *  the purpose of the program. The next few lines give a sample execution\r\n *  of the program and the resulting output. We will always include such \r\n *  lines in our programs and encourage you to do the same.\r\n *\r\n ******************************************************************************/\r\n\r\npublic class HelloWorld {\r\n\r\n    public static void main(String[] args) {\r\n        // Prints \"Hello, World\" to the terminal window.\r\n        System.out.println(\"Hello, World\");\r\n    }\r\n\r\n}\r\n', 'java', 'Never', 'public', 'Java', 'Guest', '2018-02-11 20:07:03'),
(29, 'import string\r\nimport random\r\n\r\nKEY_LEN = 20\r\n\r\ndef base_str():\r\n    return (string.letters+string.digits)   \r\ndef key_gen():\r\n    keylist = [random.choice(base_str()) for i in range(KEY_LEN)]\r\n    return (\"\".join(keylist))', 'python', 'Never', 'public', 'random letter generator python', 'Guest', '2018-02-11 20:10:40');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `register_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `username`, `password`, `register_date`) VALUES
(1, 'John Doe', 'jd@gmail.com', 'jando', '$5$rounds=535000$LvHO0lcq5tyIOtze$XddPrWW7jQvOkyoVbrLIZ.WcEOVurMw6vP69H79JX4.', '2018-02-07 00:23:13'),
(2, 'Aries', 'ariesabao05@gmail.com', 'bitwan', '$5$rounds=535000$9z26DrnS/VEmeNw7$EGd2RwkzF/Qvz1odnfYxvP6rHf6N530eG042iyvx.65', '2018-02-07 00:24:49'),
(3, 'Aries', 'ariesabao05@gmail.com', 'bitwan', '$5$rounds=535000$BROUxFz5YRDoZB8l$SaIfGWce2s9rxkZxxxkCr1RCVunBMS6XAFYAyt8DzJ7', '2018-02-07 00:26:37'),
(4, 'qwewqe', 'qweqwe', 'qweqwe', '$5$rounds=535000$1L6VFml1ICuChelS$/ujLfZebJiQl6MwVeBFGzyon/ydUWdyCIAX4IBM71w9', '2018-02-07 00:27:16'),
(5, 'dfg', 'dfasdasdg@gmail.com', 'dfghgjhkjljk', '$5$rounds=535000$Ubeof/poovTcX5OW$ZZ56piHlCVt4EheL8rKIjhg7MSiAz4NtYFfqnYHcSk3', '2018-02-07 00:28:30'),
(6, 'Aries A', 'ariesabao05@gmail.com', 'aries', '$5$rounds=535000$VQHCEVBV9ojwUOGy$lrBG/GA45QquGXKHKjB.7Pk1c8TiKwXuOc9zJk60GdC', '2018-02-07 03:55:12'),
(7, 'AriesYT', 'ariesyt@gmail.com', 'ariesyt', '$5$rounds=535000$uiTLbKJd342vhI2O$UdQsgiPlTq21f1U3CIDxF.hbLrtzvrYpJyoPlPIOM84', '2018-03-01 07:58:49'),
(8, 'AriesYT', 'ariesyt@gmail.com', 'ariesyt', '$5$rounds=535000$BKoOjp8nrbJl6Omg$vgTZQ.4jtV7IPYfrwAH/bkKCvwdcu5E8o0PVno6ukS3', '2018-03-01 07:59:31');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `paste`
--
ALTER TABLE `paste`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `paste`
--
ALTER TABLE `paste`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
