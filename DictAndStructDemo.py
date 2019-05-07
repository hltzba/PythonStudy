# encoding:utf-8
import pprint

"""
字典和结构体的学习代码，ticTacToe是五子棋游戏，不过，写着好麻烦
算了，还是不写了

"""
def ticTacToe():
    theBoard={'top-L':'','top-M':'','top-R':'',
              'mid-L':'','mid-M':'','mid-R':'',
              'low-L':'','low-M':'','low-R':''}

def CommonTest():
    myCat={"Name":"Tom","Size":"Fat","Color":"Orange","Disposition":"Loud"}
    print("My cat has "+myCat["Color"].lower()+" fur.")
    print(str(myCat.keys()))
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    count={}
    for char in message:
        count.setdefault(char,0)
        count[char]+=1
    print(count)
    pprint.pprint(count)

# birthdays demo 
def birthdaysdemo():
    print("==========birthdays demo==========")
    birthdays={"Alice":"Apr 1","Bob":"Dec 12","Carol":"Mar 4"}
    while True:
        print("输入名字查找生日，直接回车退出：")
        name=input()
        if name=='':
            print("bye from birthdays demo.")
            break
        if name in birthdays:
            print(name+"的生日时间是"+birthdays[name])
        else:
            print("我这儿没有"+name+"的生日信息，要不输入一下？")
            bday=input()
            if bday=='':
                break
            else:
                birthdays[name]=bday
                print(name+"的生日信息已加入。")


