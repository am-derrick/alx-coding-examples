import re

# Sample log data
log_data = """
[2023-10-31 08:45:12] INFO: This is an informational message
[2023-10-31 09:15:30] ERROR: An error occurred
[2023-10-31 09:30:55] WARNING: Warning message
"""

# Regular expressions for parsing log entries
log_entry_pattern = r'\[(.*?)\] (\w+): (.*)'

# Find all log entries using the regular expression
log_entries = re.findall(log_entry_pattern, log_data)

# Iterate through the log entries and extract information
for entry in log_entries:
    timestamp, log_level, message = entry
    print(f"Timestamp: {timestamp}, Level: {log_level}, Message: {message}")

