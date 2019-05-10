# encoding:utf-8
#! python3
# PhoneAndEmail.py Finds phone numbers and email addresses  on the clipboard.
import pyperclip,re,sys
phoneRegex=re.compile(r'\d{11}')
emailRegex=re.compile(r'''(
    [a-zA-Z0-9._%+-]+        #username
    @                        #symbol
    [a-zA-Z0-9.-]+           #domainname
    \.[a-zA-Z]{2,4}       #dot-something
)''',re.VERBOSE)
origintext=str(pyperclip.paste())
if origintext==None or len(origintext)==0:
    print('clipboard has no text.')
    sys.exit(0)
matches=[]
for phone in phoneRegex.findall(origintext):
    matches.append(phone)
for email in emailRegex.findall(origintext):
    matches.append(email)
if(len(matches)>0):
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')