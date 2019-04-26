# encoding:utf-8
# 猜数字
import random
secretNum=random.randint(1,20)
print("猜一个1到20的整数，你可以猜6次哦！")
for guessesTaken in range(1,7):
    print("输入你猜的数值，按回车：")
    guess=int(input())
    if guess<secretNum:
        print("太小了")
    elif guess>secretNum:
        print("太大了")
    else:
        break
if guess==secretNum:
    print("猜对啦，就是"+str(guess)+"，一共猜了"+str(guessesTaken)+"次。")
else:
    print("猜6次都猜不对哎")