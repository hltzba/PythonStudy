# encoding:utf-8
import datetime
import re
import os

def RemoveLog(dayslen):
    '''
    now_time = datetime.datetime.now().strftime("%Y%m%d")
    
    filename = "access_"+now_time+".log"
    print(filename)
    # 正则表达式获取数字
    innernum = re.sub(r"\D", "", filename)  # 获取数字
    print("inner number:"+innernum)
    '''
    # 计算时间间隔
    timespan = datetime.timedelta(days=dayslen)  # 设置时间间隔30
    targettime = datetime.datetime.now()-timespan
    print("30天前的日期是："+targettime.strftime("%Y%m%d"))
    # 获取文件
    log_dir="/usr/local/nginx/logs/logs_bak/"
    #log_dir = "C:\\logs_bak\\"
    filelist = []
    for dirs in os.walk(log_dir):
        for file in dirs[2]:
            filelist.append(file)
    for item in filelist:
        targetnum=int(targettime.strftime("%Y%m%d"))
        currentnum=int(re.sub(r"\D","",item))
        if targetnum>currentnum:
            os.remove(log_dir+item)
            print(item+"已删除")
        
        

if __name__ == "__main__":
    dayslen=30
    RemoveLog(dayslen)
