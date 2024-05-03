import re, pyperclip

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

phones = phoneRegex.finditer(text)
emails = emailRegex.finditer(text)

print("\nPhone Numbers: ")
for phone in phones:
    start = phone.start()
    end = phone.end()
    print(text[start:end])

print("\nEmail address: ")
for email in emails:
    start = email.start()
    end = email.end()
    print(text[start:end])
print("\n")