# encoding:utf-8
#! python3
# renameDates.py - Rename filenames with American MM-DD-YYYY date format to Chinese YYYY-MM-DD
import re,shutil,os
workdir='C:\\Temp\\'
#Create a regex that matches files with American date format.
datePattern=re._compile(r'''^(.*?)     # all text before the date
((0|1)?\d)-                            # One or two digits for the month
((0|1|2|3)?\d)-                        # One or two digits for the day
((19|20)\d\d)                          # Four digits for the year
(.*?)$                                 # all text after the date 
''',re.VERBOSE)# 传入VERBOSE参数则允许正则表达式允许空白字符和注释，增加可读性
# TODO:Loop over the files in the working directory
for amerFilename in os.listdir(workdir):
    mo=datePattern.search(amerFilename)
# TODO：Skip files without a date.
    if mo==None:
        continue
# TODO: Get different parts of the filename.
    beforePart=mo.group(1)
    monthPart=mo.group(2)
    dayPart=mo.group(4)
    yearPart=mo.group(6)
    afterPart=mo.group(8)
# TODO: Form the Chinese-style filename.
    chnFilename=beforePart+yearPart+'-'+monthPart+'-'+dayPart+afterPart    
# TODO: Get the full,absolute file paths.
    amerFilename=os.path.join(workdir,amerFilename)
    chnFilename=os.path.join(workdir,chnFilename)
# TODO: Rename the files.
    print('Renamingg %s to %s...'%(amerFilename,chnFilename))
    shutil.move(amerFilename,chnFilename)