#! /usr/bin/env python3
"""

    author: python.wonder.woman@gmail.com
    wersja EN
    this is a simple script which is using:
                random module,
                def functions,
                regex

"""

import random
import re

def hello(login):
    email = input("What is your email address?: ")

    def isEmail():
        emailRegex = re.compile(r'\w+[.|_]\w+@\w+.\w+')
        print(emailRegex.findall(email))
        print("\n")
        if :
            print("")

    isEmail()

    set_pass = input("Enter 3 uppercase letters: ")
    set_pass2 = input("Enter 3 spacial characters: ")
    passwd = random.randint(1, 73)

    print("Hello there user: " + login + ".")
    print("Your email addrress is: " + email)
    print("Your login to the system is: " + login)
    print("Your password is: " + set_pass + str(passwd)*2 + set_pass2 + str(passwd))
    print("Your can reset your password anytime using 'Forgot password button'.")



hello('python.wonder.woman@gmail.com')