import re

# Regular expression for email validation
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    # Use the re.match() function to check if the email matches the pattern
    if re.match(email_pattern, email):
        return True
    else:
        return False

# Example usage
email1 = "john.doe@example.com"
email2 = "invalid_email@.com"
email3 = "another.example@email"
email4 = "dampire@sandtech.com"

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
