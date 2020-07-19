#Phone validation
#valid phone no. format is xxx-xxx-xxxx Ex. 333-222-4444

import re

def is_it_phone_no():
    phone = input("Enter the phone number: ")
    if re.search("\d{3}-\d{3}-\d{4}", phone) and len(phone)==12 :
        print("It is a phone number"
    else:
        print('It is not a phone number')

is_it_phone_no()


