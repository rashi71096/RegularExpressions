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


print('Regular Expression')

answer=='YES'

while answer=='YES':
    print('\n1.To get user name from JSON file \n2.To get URL from given string  \n3.To get date and time from string \n4.Password validation \n5.Aadhaar No validation \n6.Email validation \n7.Phone No validation /n')
    value=int(input('Enter your choice: '))
    if value==1:
        get_user_name()
    elif value==2:
        url=input("Enter your string")
        is_valid_url(url)
    elif value==3:
        ans=input("Enter your string")
        is_date(ans)
    elif value==4:
        password_validation()
    elif value==5:
        aadhaar = input("Enter Aadhaar No")
        is_valid_aadhar(aadhaar)
    elif value==6:
        Temp = email_validation()
        print(Temp)
    elif value==7:
        Temp = is_it_phone_no()
        print(Temp)
    else:
        print("Wrong Choice")
        
    print("Do you want to continue? if Yes enter YES and for No enter NO")
    answer=input()
