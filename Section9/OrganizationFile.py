# encoding=utf-8
#! python3
# OrganizationFile.py 
import shutil,os,zipfile
def copyFile():
    os.chdir('C:\\')
    shutil.copy('C:\\ActLog.txt','C:\\Temp')
    shutil.copy('C:\\ActLog.txt','C:\\Temp\\ActLog2.txt')

def copyDir():
    os.chdir('C:\\')
    shutil.copytree('C:\\Temp','C:\\Temp_Backup')

def moveFile():
    shutil.move('C:\\ActLog.txt','C:\\Temp\\ActLog_Move.txt')

def DelFile():
    os.unlink('C:\\Temp_Backup\\ActLog2.txt')

def DelEmptyDir():
    os.rmdir('C:\\Temp_Backup')

def DelDir():
    shutil.rmtree('C:\\Temp_Backup')

def dirWalk():
    for foldername,subfolders,filenames in os.walk('C:\\Python37'):
        print('当前文件夹：'+foldername)
        for subfolder in subfolders:
            print('子文件夹：'+subfolder)
        for filename in filenames:
            print('文件：'+filename)

def viewZipFileInfo():
    exampleZip=zipfile.ZipFile('C:\\ILSpy.zip')
    print(exampleZip.namelist())
    mainfile=exampleZip.getinfo('ILSpy/ILSpy.exe')
    filesize=mainfile.file_size
    compresssize=mainfile.compress_size
    print('ILSpy.exe file size is %sKB,Compressed size is %sKB.'%(filesize/1024,compresssize/1024))
    print('Compressed file is %sx smaller!'%(round(filesize/compresssize,2)))
    exampleZip.close()

#copyFile()
#copyDir()
#moveFile()
#DelFile()
#DelEmptyDir()
#DelDir()
#dirWalk()
viewZipFileInfo()