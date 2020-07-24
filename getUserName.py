#Extract user name from JSON- Source.json
#Fetch User Name attribute from uploaded JSON.

import json
import re

def get_user_name():
  
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