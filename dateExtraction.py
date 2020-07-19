#Date Extraction from String
#Format of date to be extracted YYYY-MM-DD ex: My DOB is 1996-10-07 and current date is 2020-07-20
#Output: 1996-10-07, 2020-07-20

import re, datetime

def is_date(string_input):
    
    match = re.findall('\d{4}-\d{2}-\d{2}', string_input)
    if(len(match)>0):
        print('The string ',string_input," has the following dates:\n")
        for dateMatched in match:
            date = datetime.datetime.strptime(dateMatched, '%Y-%m-%d')
            print(date)
        return True
    else:
        print('No dates present in string')
        return False
        
