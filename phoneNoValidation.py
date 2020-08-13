#Phone validation
#valid phone no. format is xxx-xxx-xxxx Ex. 333-222-4444

import re

def is_it_phone_no():
    phone = input("Enter the string to find does it contain phone no or not: ")
    phone_match = re.search("\d{3}-\d{3}-\d{4}", phone)
    if phone_match is not None:
        phoneNo = phone_match.group()
        print('This string contains valid phone no and it is ' + phoneNo )
        return True
    else:
        print('This string does not contain the valid phone no')
        return False




