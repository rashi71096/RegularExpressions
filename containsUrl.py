#To get URL from the given string 
#example = "To study the Regular Expression you can go to "https://w3resource.com" and for any problem you can refer "http://github.com" as well."

import re

def is_valid_url(text):

    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    print("Original string: ",text)
    if(urls == []):
        print('This string does not contain any valid URL')
    else:
        print("URL in the string: ",urls)
        