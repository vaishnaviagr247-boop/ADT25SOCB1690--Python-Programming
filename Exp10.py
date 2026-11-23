# Step 1: Import the regular expression module
import re

# Step 2: Store the text containing email addresses
text = """
Hello Om,
Please contact us at support@example.com
or admin@company.org.
"""

# Step 3: Create a pattern to find email addresses
pattern = r'[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Step 4: Find all email addresses in the text
emails = re.findall(pattern, text)

# Step 5: Display a heading
print("Email addresses found:")

# Step 5: Display the extracted email addresses
for email in emails:
  print(email)
for email in emails:
  print(email)