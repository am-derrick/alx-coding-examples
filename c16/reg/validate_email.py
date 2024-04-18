import re

#email pattern
email_pattern = r'^[a-zA-Z0-9._%+-]@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# function to check if email is valid
def email_is_valid(email):
    if re.match(email_pattern, email):
        return True
    else:
        return False


email1 = "john.doe@email.com"
email2 = "dampire@sandtech.com"
email3 = "hey@.com"

if email_is_valid(email1):
    print(f"{email1} is valid.")
else:
    print(f"{email1} is invalid.")

if email_is_valid(email2):
    print(f"{email2} is valid.")
else:
    print(f"{email2} is invalid.")

if email_is_valid(email3):
    print(f"{email3} is valid.")
else:
    print(f"{email3} is invalid.")
