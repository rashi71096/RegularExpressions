# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:08:55 2020

@author: Sudarshan,Shweta
"""

from emailValidation import email_validation
from containsUrl import is_valid_url
from getUserName import get_user_name
from aadharValidation import is_valid_aadhar
from dateExtraction import is_date
from passwordValidation import password_validation
from phoneNoValidation import is_it_phone_no

print('Regular Expression')
answer = 'Y'

while answer=='Y':
    print('\n1.To get user name from JSON file \n2.To get URL from given string  \n3.To get date and time from string \n4.Password validation \n5.Aadhaar No validation \n6.Email validation \n7.Phone No validation /n')
    value=input('Enter your choice: ')
    if value == '1':
        get_user_name()
    elif value == '2':
        url=input("Enter your string string for checking does it contain URL \n")
        is_valid_url(url)
    elif value == '3':
        ans=input("Enter your string for date and time checking \n")
        is_date(ans)
    elif value == '4':
        password_validation()
    elif value == '5':
        aadhaar = input("Enter string for checking is there aadhar no exists")
        is_valid_aadhar(aadhaar)
    elif value == '6':
        email_validation()
    elif value == '7':
        is_it_phone_no()
    else:
        print("Wrong Choice")
        
    print("Do you want to continue? if Yes enter Y and for No enter any other key: ")
    answer=input()

