# encoding:utf-8
myCat={"Name":"Tom","Size":"Fat","Color":"Orange","Disposition":"Loud"}
print("My cat has "+myCat["Color"].lower()+" fur.")

# birthdays demo 
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
