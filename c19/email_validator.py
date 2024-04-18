import re

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    if re.match(email_pattern, email):
        return True
    else:
        return False


email1 = "johndoe@example.com"
email2 = "dampire@sandtech.com"
email3 = "invalid_email@.com"
email4 = "example.example@email"

if is_valid_email(email1):
    print(f"{email1} is a valid email.")
else:
    print(f"{email1} is not a valid email.")

if is_valid_email(email2):
    print(f"{email2} is a valid email.")
else:
    print(f"{email2} is not a valid email.")

if is_valid_email(email3):
    print(f"{email3} is a valid email.")
else:
    print(f"{email3} is not a valid email.")

if is_valid_email(email4):
    print(f"{email4} is a valid email.")
else:
    print(f"{email4} is not a valid email.")
