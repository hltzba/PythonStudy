# encoding:utf-8
def collatz(number):
    if number%2==1:
        return 3*number+1
    else:
        return number//2
print("考拉次猜想===输入一个大于0的正整数，最终会算出一个结果为1的结果：")
while True:
    try:
        t=int(input())
        if t<1:
            print("输入错误，请输入一个大于0的正整数")
            continue
        else:
            break
    except ValueError:
        print("输入错误，请输入一个大于0的正整数")

while True:
    t=collatz(t)
    print("本次运算结果："+str(t))
    if t==1:
        print("结束！")
        break