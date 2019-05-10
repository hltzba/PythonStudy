# encoding:utf-8
#! python3
# stripRegex.py string trim
import re
while True:
    print("enter your content string(Enter 'exit()' to exit program.):")    
    content=input()
    if content=='exit()':
        break
    prefixtrimRegex=re.compile(r'^\s*')
    tailtrimRegex=re.compile(r'\s*$')
    content=prefixtrimRegex.sub('',content)
    content=tailtrimRegex.sub('',content)
    print(content+' length:'+str(len(content)))
