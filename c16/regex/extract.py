import re
import requests

# URL of the web page to scrape
url = "https://www.randomlists.com/email-addresses"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the HTML content of the web page
    html_content = response.text

    # Regular expression pattern to extract all email addresses from the web page
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    # Use re.findall to extract all email addresses matching the pattern
    email_addresses = re.findall(email_pattern, html_content)

    # Print the extracted email addresses
    for mail in email_addresses:
        print("Email: ", mail)
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)

