# encoding:utf-8
def ReadAnimalsToList():
    cats=[]
    while True:
        print("来，请输入一个猫的名字，不想玩了就直接回车：")
        name=input()
        if name=='':
            break
        cats=cats+[name]
    print("来看看猫咪们都有哪些名字："+str(cats))
        
zoo=['cat','bat','rat','elephant']
print("现在有这些个动物:"+str(zoo))
print("切片取第2个到第3个："+str(zoo[1:3]))
print("现在有"+str(len(zoo))+"只动物。")
print("加个1，2，3的列表吧："+str(zoo+[1,2,3]))
print("把小动物们翻个倍吧："+str(zoo*2))
del zoo[2]
print("把第三只动物删掉还剩下什么呢:"+str(zoo))
print("迭代一下列表下标")
for i in range(len(zoo)):
    print("第"+str(i+1)+"只动物是 "+zoo[i])
print("cat在吗："+str('cat' in zoo))
print("rat被删了，那它还在吗："+str('rat' in zoo))
print("elehant是不是不在呀？"+str('elephant' not in zoo))
catfeature=['fat','black','loud']
size,color,disposition=catfeature
print("多重赋值技巧，来看看猫猫的特点吧,胖否："+size+" 颜色："+color+" 性格："+disposition)
print("bat排老几呀："+str(zoo.index('bat')))
zoo.append('dog')
print("给动物园后面加一只dog吧："+str(zoo))
zoo.insert(2,'rat')
print("我们还是把rat放回第三个位置吧："+str(zoo))
zoo.remove('dog')
print("动物园里怎么可以有dog，删除它："+str(zoo))
zoo.sort()
print("动物园排个序："+str(zoo))
zoo.sort(reverse=True)
print("动物园排个升序："+str(zoo))
#print("===============\n接下来，我们用列表做个反复输入的小功能：")
#ReadAnimalsToList()

#逗号代码练习
print(str(zoo[:-1])[1:-1]+" and "+zoo[-1])

#打印桃心
grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]
for y in range(len(grid[0])):
    strp=''
    for x in range(len(grid)):
        strp+=grid[x][y]
    print(strp)
