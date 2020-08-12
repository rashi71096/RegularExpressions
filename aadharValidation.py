#Aadhar Number Validation
#Valid aadhar format is XXXX XXXX XXXX Ex. 5231 8352 5406

import re

def is_valid_aadhar(aadharInput):
    valid_aadhar = re.search('\d{4} \d{4} \d{4}', aadharInput)
    print("Input for aadhar validation: ",aadharInput)
    if valid_aadhar is not None:
        adhar  = valid_aadhar.group()
        print("This string contain valid adhar number and the adhar no is " + adhar )
        return True
    else:
        print('This string does not contain the valid adhar number')
        return False
        
        
