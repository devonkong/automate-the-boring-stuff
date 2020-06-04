#! python3
# Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = f"* {lines[i].lstrip('* ')}""  # Strips existing bullet points and spaces (if any) for consistency and adds bullet points
    
text = '\n'.join(lines)

pyperclip.copy(text)