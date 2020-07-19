# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:08:55 2020

@author: Rashi
"""

from emailValidation import email_validation
from containsUrl import is_valid_url
from getUserName import get_user_name
from aadharValidation import is_valid_aadhar
from dateExtraction import is_date
from passwordValidation import password_validation
from phoneNoValidation import is_it_phone_no

print("Following is the user names in the  json file :")
get_user_name()
is_valid_url('https://www.google.com')
email_validation()
is_valid_aadhar('5231 8352 5406')
is_date('My DOB is 1996-10-07 and current date is 2020-07-20')
password_validation()
is_it_phone_no()
