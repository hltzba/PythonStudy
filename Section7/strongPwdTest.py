# encoding:utf-8
#! python3
# strongPwdTest.py strong password must be no less 8 chars in length,with both upper and lower case chars,and at least one digit.
# please reference regexDemo.py PasswordTest() method
import re
testresult=''
while True:
    print("enter your strong password for test(Enter 'exit()' to exit program.):")
    testresult=''
    pwd=input()
    if pwd=='exit()':
        break
    spaceRegex=re.compile(r'^\s|\s$')
    if spaceRegex.search(pwd)!=None:
        print('password can not contains spaces!')
        continue
    else:
        testresult+='spaces test: OK \n'
    lengthRegex=re.compile(r'\S{8,}')
    if lengthRegex.search(pwd)==None:
        print('Password must be no less 8 chars in length.')
        continue
    else:
        testresult+='length test: OK \n'
    lowercaseRegex=re.compile(r'[a-z]+')
    if lowercaseRegex.search(pwd)==None:
        print('Password must contains lower case char.')
        continue
    else:
        testresult+='lower case char test: OK \n'
    break

print(testresult)