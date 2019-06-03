# encoding:utf-8
# 字符串练习
zoo=['cat','bat','rat','elephant']
def isX():
    print("来，输入你的年龄吧：")
    while True:
        age=input()
        if age.isdecimal():
            print("你原来"+age+"岁了呀")
            break
        else:
            print("年龄只能是数字")
    print("来，输入你的密码吧：")
    while True:
        pwd=input()
        if pwd.isalnum():
            print("哦~你的密码是"+pwd+"呀")
            break
        else:
            print("密码只能是字母加数字的组合哦")

def SplitAndJoin():
    global zoo
    print(','.join(zoo))
    sentence='My name is Jimmy.'
    print(sentence.split('.'))

def LongSentenceSplit():
    sentence='''Dear Alice,
How have you been?
Please don't drink it!
Sincerely,
Jimmy'''
    print(sentence.split('\n'))

def AlignText():
    spam='Hello'
    print(spam.rjust(10))
    print(spam.rjust(5))
    print(spam.rjust(4))
    print(spam.ljust(10))
    print(spam.center(11))
    print(spam.center(11,'*'))

def PrintPicnicList(leftwidth,rightwidth):
    picnicitems={'sanwiches':4,'appples':12,'cups':4,'cookies':180}
    print('PICNIC ITEMS'.center(leftwidth+rightwidth,'='))
    for k,v in picnicitems.items():
        print(k.ljust(leftwidth,'.')+str(v).rjust(rightwidth,'.'))

def LikeCSharpTrim():
    spam=' SpamSpamBaconSpamEggsSapmSpam '
    print(spam.lstrip())
    print(spam.rstrip())
    print(spam.strip())
    print(spam.strip().strip('ampS'))

def PrintTables():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]
    for y in range(len(tableData[0])):
        pstr=''
        for x in range(len(tableData)):
            if x==0:
                pstr+=tableData[x][y].rjust(8)
            elif x==1:
                pstr+=tableData[x][y].center(8)
            else:
                pstr+=tableData[x][y].ljust(5)
        print(pstr)

#isX()
#SplitAndJoin()
#LongSentenceSplit()
#AlignText()
#PrintPicnicList(12,12)
#LikeCSharpTrim()
PrintTables()