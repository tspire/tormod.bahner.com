#!/usr/bin/env python3
# coding: utf-8
# pylint: disable=invalid-name
"""Simple CGI Script to retrieve and store email messages"""

import os
import datetime

import cgi
# Two following lines are for development, not production.
import cgitb
cgitb.enable()

# Set the current time
NOW = str(datetime.datetime.now())
OUTPUT = '../quotes/quote.txt'
REDIR = os.getenv('HTTP_REFERER', 'https://tormod.bahner.com/')

# Fetch the data from the form sent here
form = cgi.FieldStorage()

# Extract the values we want to use.
# Make sure they are converted to strings,
# using the str() method, to make reception
# of data secure.
name = str(form.getvalue('name'))
email = str(form.getvalue('email'))
msg = str(form.getvalue('msg'))

# Generate text string to write to file.
txt = "%s\n" % NOW
txt += "name: %s\n" % name
txt += "email: %s\n" % email
txt += "*" * 80 + "\n"
txt += msg + "\n"
txt += "*" * 80 + "\n"
txt += '\n'

# Write to file, using "a" to only append, and
# *NOT* overwrite anything.
with open(OUTPUT, "a") as quote:
    quote.write(txt)

# Sign off and say thank you.
print("""Content-Type: text/html;charset=utf-8
<!DOCTYPE html>
<html>
<head>
   <!-- HTML meta refresh URL redirection -->
   <meta http-equiv="refresh"
   content="3; url=%s">
</head>
<body>
   Takk for dine input, %s
</body>
</html>
""" % (REDIR, name))
