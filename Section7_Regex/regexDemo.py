# encoding:utf-8
#! python3
#regexDemo.py regex common demo program.
import re

def isPhoneNumber():
    phoneNumRegex=re.compile(r'(\d{3})-(\d{3}-\d{4})')
    rel=phoneNumRegex.search('My number is 415-555-4242.')
    print('Phone number found:'+rel.group())
    print(rel.groups())
    print(rel.group(2))

def pipeOperator():
    heroRegex=re.compile(r'Batman|Tina Fey')
    rel=heroRegex.search('Batman and Tina Fey.')
    print(rel.group())

def prefixMatch():
    batRegex=re.compile(r'Bat(man|bat|mobile|copter)')# matching a word with 'Bat' prefix.
    rel=batRegex.search('Batmobile lost a wheel.')
    print(rel.group())
    print(rel.group(1))

def OptionalMatch():
    batRegex=re.compile(r'Bat(wo)?man')#'wo' is optional match group
    rel=batRegex.search('The Adeventures of Batman')
    print(rel.group())
    rel=batRegex.search('The Adventures of Batwoman')
    print(rel.group())

    batSomeTimesRegex=re.compile(r'Bat(wo)*man')#matching 'wo' group 0 time or some times.
    rel=batSomeTimesRegex.search('The Adeventures of Batman')
    print(rel.group())
    rel=batSomeTimesRegex.search('The Adventures of Batwoman')
    print(rel.group())
    rel=batSomeTimesRegex.search('The Adventures of Batwowowowoman')
    print(rel.group())

    batMustbeRegex=re.compile(r'Bat(wo)+man')#matching 'wo' group >= 1 time.
    rel=batMustbeRegex.search('The Adeventures of Batman')
    print("匹配结果为空："+str(rel==None))
    rel=batMustbeRegex.search('The Adventures of Batwoman')
    print(rel.group())
    rel=batMustbeRegex.search('The Adventures of Batwowowowoman')
    print(rel.group())

def GreedyAndGenerousMatch():
    greedyHaRegex=re.compile(r'(Ha){3,5}')
    rel=greedyHaRegex.search('HaHaHaHaHa')
    print(rel.group())
    nongreedyHaRegex=re.compile(r'(Ha){3,5}?')
    rel=nongreedyHaRegex.search('HaHaHaHaHa')
    print(rel.group())

def findAllTest():
    isPhoneNumRegex=re.compile(r'\d{11}')
    #rel=isPhoneNumRegex.search('My mobile phone number is 13812341234,and another is 19912341234.')
    print(isPhoneNumRegex.findall('My mobile phone number is 13812341234,and another is 19912341234.'))

def wildcardMatch():
    wildcardRegex=re.compile(r'.at')
    print(wildcardRegex.findall('The cat in the hat sat on the flat mat.'))

def allTextMatch():
    nameRegex=re.compile(r'FirstName:(.*) LastName:(.*)')
    rel=nameRegex.search('FirstName:Jimmy LastName:Wang')
    print(rel.group(1))
    print(rel.group(2))

def allTextNonGreedyMatch():
    text='<To serve man> for dinner.>'
    nongreedyRegex=re.compile(r'<.*?>')
    rel=nongreedyRegex.search(text)
    print(rel.group())
    greedyRegex=re.compile(r'<.*>')
    rel=greedyRegex.search(text)
    print(rel.group())

def dotAllMatch():
    text='Serve the public trust.\nProtect the innocent.\nUphold the law.'
    noNewLineRegex=re.compile(r'.*')
    rel=noNewLineRegex.search(text)
    print(rel.group())
    print(''.center(10,'='))
    newLineRegex=re.compile(r'.*',re.DOTALL)
    rel=newLineRegex.search(text)
    print(rel.group())

def IgnoreCaseMatch():
    icRegex=re.compile(r'robocop',re.I)
    print(icRegex.search('RoboCop is part man, part machine, all cop.').group())
    print(icRegex.search('ROBOCOP protects the innocent.').group())
    print(icRegex.search('Al, why does your programming book talk about robocop so much?').group())

def SubstitudeTest():
    origintext='Agent Alice gave the secret documents to Agent Bob.'
    nameRegex=re.compile(r'Agent \w+')
    print(re.findall(r'Agent \w+',origintext))
    subtext=nameRegex.sub('Jimmy Wang',origintext)
    print(subtext)
    print(''.center(18,'='))
    origintext='Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'
    nameRegex=re.compile(r'Agent (\w)\w*')
    subtext=nameRegex.sub(r'\1****',origintext)
    print(subtext)

def UpperAndLowerCase():
    while True:
        print('enter test string,exit() to exit program:')
        content=input()
        if content=='exit()':
            break
        regex=re.compile(r'([a-z]+)([A-Z]+)')
        if regex.search(content)==None:
            print('不匹配')
            continue
        else:
            print('匹配正确')
            break

def PasswordTest():
    while True:
        print('enter test string,exit() to exit program:')
        content=input()
        if content=='exit()':
            break
        regex=re.compile(r'^(?=.*[0-9].*)(?=.*[A-Z].*)(?=.*[a-z].*).{3,}$')
        #regex=re.compile(r'^(?=[0-9]+)(?=[A-Z]+)(?=[a-z]+).{3,}$')
        if regex.search(content)==None:
            print('不匹配')
            continue
        else:
            print('匹配正确')
            break
#isPhoneNumber()
#pipeOperator()
#prefixMatch()
#OptionalMatch()
#findAllTest()
#wildcardMatch()
#allTextMatch()
#allTextNonGreedyMatch()
#dotAllMatch()
#IgnoreCaseMatch()
#SubstitudeTest()
#UpperAndLowerCase()
PasswordTest()