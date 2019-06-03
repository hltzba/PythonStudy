# encoding:utf-8
#! python3
# iodemo.py 
import os,shelve
def workDir():
    print(os.getcwd())
    newpath=os.path.join('D:\\','python','PythonStudy')
    print(newpath)
    os.chdir(newpath)
    print(os.getcwd())

def makedir():
    os.chdir(os.path.join('D:\\','python'))
    os.mkdir('output')

def makedirWithAllPath():
    os.chdir(os.path.join('D:\\','python'))
    os.makedirs('output\\delicious\\walnut\\waffles')#会创建所有缺失的目录

def absPath():
    print('当前绝对路径：'+os.path.abspath('.'))
    print('.是绝对路径吗？'+str(os.path.isabs('.')))
    print('那调用一下abs呢？'+str(os.path.isabs(os.path.abspath('.'))))
    relpath=os.path.relpath(os.getcwd(),'D:\\')
    print('当前工作目录到D盘根目录的相对路径是：'+relpath)
    path='D:\python\PythonStudy\PythonStudy\Section8\iodemo.py'
    print(os.path.dirname(path))
    print(os.path.basename(path))
    print(os.path.split(path))
    print(path.split(os.path.sep))

def viewDirDetails():
    print('文件名'.ljust(25,' ')+'大小')
    for filename in os.listdir(os.path.abspath('.')):
        size=os.path.getsize(os.path.join(os.path.abspath('.'),filename))
        print(filename.ljust(25,' ')+str(size))

def dirIsValid():
    if os.path.exists(os.path.abspath('.')):
        print(os.path.abspath('.')+"  存在")
    else:
        print(os.path.abspath('.')+"  不存在")

    filepath=os.path.join(os.path.abspath('.'),'LICENSE2')
    if os.path.exists(filepath):
        print(filepath+"  存在")
    else:
        print(filepath+"  不存在")

def ReadFile():
    file=open('D:\\Hello.txt','r')
    content=file.read()
    print(content)
    file=open('D:\\Hello.txt','r')
    contentlines=file.readlines()
    print(contentlines)
    
def WriteFile():
    file=open('D:\\hello.txt','a')
    file.write('hello world\n')
    file.write('hello world2\n')

def shelveTest():
    file=shelve.open('D:\\shelvetest.dat')
    config={'ConnectionString':'sdada','ProviderName':'NativeSqlClient'}
    file['config']=config
    file.close()
    reader=shelve.open('D:\\shelvetest.dat')
    print(reader['config'])
    print(list(reader.keys()))
    print(list(reader.values()))
    

#workDir()
#makedir()
#makedirWithAllPath()
#absPath()
#viewDirDetails()
#dirIsValid()
#ReadFile()
#WriteFile()
shelveTest()