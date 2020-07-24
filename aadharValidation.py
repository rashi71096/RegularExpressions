#Aadhar Number Validation
#Valid aadhar format is XXXX XXXX XXXX Ex. 5231 8352 5406

import re

def is_valid_aadhar(aadharInput):
    valid_aadhar = re.search('^[2-9]{1}[0-9]{3}\\s[0-9]{4}\\s[0-9]{4}$', aadharInput)
    print("Input for aadhar validation: ",aadharInput)
    if(valid_aadhar):
        print(aadharInput," is a valid aadhar number")
        return True
    else:
        print(aadharInput, " is not a valid aadhar number")
        return False
        