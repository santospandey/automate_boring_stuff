
# "Matches pattern like 415-555-4242"
# def isPhoneNo(text):
#     if len(text) != 12:
#         return False
#     if text[3] != '-' or text[7] != '-':
#         return False
#     for i in range(12):
#         if i == 3 or i == 7:
#             continue
#         if not text[i].isdecimal():
#             return False
#     return True

# phoneNumbers = [
#     '415-555-4242',
#     '41a-555-4242',
#     'abcd',
#     '415-55-4242',
#     '000-999-4042'
# ]

# for phone in phoneNumbers:
#     if isPhoneNo(phone):
#         print(f"{phone} is valid phone number")
#     else:
#         print(f"{phone} is not valid phone number")

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     print(chunk, len(chunk))
#     if isPhoneNo(chunk):
#         print(f"Phone number found: {chunk}")

import re
phoneNoRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
phones = phoneNoRegex.finditer(message)

for phone in phones:
    s = phone.start()
    e = phone.end()
    print(message[s:e])