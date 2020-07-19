# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:08:55 2020

@author: Rashi
"""


#To get URL from the given string 
#example = "To study the Regular Expression you can go to "https://w3resource.com" and for any problem you can refer "http://github.com" as well."
def is_valid_url(text):
    import re
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    print("Original string: ",text)
    if(urls == []):
        print('This string does not contain any valid URL')
    else:
        print("URL in the string: ",urls)
        


#To get all the users who has given answers in the course
def get_user_name():
    import json
    import re
    with open('./Source.json') as access_json:
        read_content = json.load(access_json)
    reObj = re.compile('display_name')
    question_access = read_content['results']
    for question_data in question_access:
        replies_access = question_data['replies']
        for replies_data in replies_access:
            user=replies_data['user']
            for key in user.keys():
                if(reObj.match(key)):
                    print (user[key])
                    
def is_valid_aadhar(aadharInput):
    import re
    valid_aadhar = re.search('^[2-9]{1}[0-9]{3}\\s[0-9]{4}\\s[0-9]{4}$', aadharInput)
    print("Input for aadhar validation: ",aadharInput)
    if(valid_aadhar):
        print(aadharInput," is a valid aadhar number")
        return True
    else:
        print(aadharInput, " is not a valid aadhar number")
        return False
        
    

def is_date(string_input):
    import re, datetime
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
        


print("Following is the user names in the  json file :")
get_user_name()

string_input=input('Please enter any string to check if it contains any link in it: ')
if(string_input):
    is_date(string_input)
