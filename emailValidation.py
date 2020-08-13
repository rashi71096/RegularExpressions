#Email validation
#valid email format is xxx@xxx.xx Ex. ssu@gmail.com

import re

def email_validation():
    email = input("Enter the string to check does it conatain email or not : ")
    valid_email = re.search("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email)
    if valid_email is not None:
        print("This string conatain valid email address and email address is ", valid_email.group())
        return True
    else:
        print('This sting does not contain valid email address')


