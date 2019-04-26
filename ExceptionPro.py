# encoding:utf-8
def DivisionTest(divideby):
    try:
        return 42/divideby
    except ZeroDivisionError:
        print("除0啦~")

rel=DivisionTest(0)
print("42/?的结果："+str(rel))