import re

def is_valid_email(email):
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(regex, email):
        print("True") 
    if "@" in email and ".com" in email:
        return True
    print("False")
is_valid_email("user@domain.com") #True
is_valid_email("user@domain") #False