import re

# Sample log data
log_data = """
[2024-29-01 15:43:09] INFO: This is an info message.
[2024-29-01 15:45:10] ERROR: An error occured.
[2024-30-01 15:50:09] WARNING: Renew your Spotify subscription.
[2024-31-01 15:43:09] URGENT: Your rent is due.
"""

log_data_pattern = r'\[(.*?)\] (\w+): (.*)'

log_entries = re.findall(log_data_pattern, log_data)

for entry in log_entries:
    timestamp, log_level, message = entry
    print(f"Timestamp: {timestamp}, level: {log_level}, Message: {message}!")
