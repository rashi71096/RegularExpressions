#Password Validation
#Password should contain numbers,capital letter,small letter,special character and having length greater than 8

import re

def password_validation():
        password = input("Please enter the password: ")
        if len(password) < 8:
            print("Your password should contain at least 8 letters")
        elif re.search('[0-9]',password) is None:
            print("Your password should have number in it")
        elif re.search('[A-Z]',password) is None:
            print("Your password should have a capital letter in it")
        elif re.search('[a-z]',password) is None:
            print("Your password should have a small letter in it")
        elif re.search('[@$!%*#?&]',password) is None:
            print("Your password should have a special letter in it")
        else:
            print("Your password is perfect!")

password_validation()

