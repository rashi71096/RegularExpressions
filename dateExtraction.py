#Date Extraction from String
#Format of date to be extracted YYYY-MM-DD ex: My DOB is 1996-10-07 and current date is 2020-07-20
#Output: 1996-10-07, 2020-07-20

import re

def is_date(string_input):
    #string_input = ' dlkdfw 2018-09-12 00:57 some-alphanumeric-charecter'
    match = re.search('\d{4}-\d{2}-\d{2} \d{2}:\d{2}', string_input)
    if match is not None:
        date = match.group()
        #print('Input string is ' + string_input)
        print('Date and time from the input string are ' + date)
        return True
    else:
        print('This string does not have the date and time')
        return False
        
