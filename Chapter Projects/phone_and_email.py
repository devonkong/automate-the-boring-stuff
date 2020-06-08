#! python3
# phone_and_email.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

# Create phone regex
phone_regex = re.compile(r"""(  # 0450 555 555 / 0450555555 / 61450555555
(61|\+61)?                        # Country code
\s?                             # Separator
(0?4\d{2})                        # First four digits
\s?                             # Separator
(\d{3})                         # Three digits
\s?                             # Separator
(\d{3})                         # Last three digits
)""", re.VERBOSE)

# Create email regex
email_regex = re.compile(r"""(
[a-zA-Z0-9.-_+%]+               # Username
@                               # @ symbol
[a-zA-Z0-9.-]+                  # Domain name
(\.[a-zA-Z]+)                   # TLD
)""", re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())

matches = []
for groups in phone_regex.findall(text):
    phone_num = ' '.join([groups[2], groups[3], groups[4]])
    if groups[1] != '':
        phone_num = '0' + phone_num
    matches.append(phone_num)
    
# Add a newline between phone numbers and emails    
matches.append('')
    
for groups in email_regex.findall(text):
    matches.append(groups[0])
    
# Copy results to the clipboard
if len(matches) > 1: 
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')