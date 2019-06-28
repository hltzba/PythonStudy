# encoding:utf-8
#! python3
# section15.py - 
import datetime,time,threading,subprocess
def showdatetime():
    now=datetime.datetime.now()
    print(now)

def unixtime2datetime():
    now=datetime.datetime.fromtimestamp(time.time())
    print(now)

def beforedate():
    datedelta=datetime.timedelta(days=-10)
    targetdate=datetime.datetime.now()+datedelta
    print('10天前的时间是：%s'%str(targetdate))

def timeDuring():
    datedelta=datetime.timedelta(days=-10)
    targetdate=datetime.datetime.now()+datedelta
    during=datetime.datetime.now()-targetdate    
    print(during.days)

def threadSleep():
    i=1
    while(i<10):
        print(datetime.datetime.now())
        i+=1
        time.sleep(1)

def formatdatetime2str():
    showstr=datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    print(showstr)
    print(datetime.datetime.now().strftime('%B,%d of %Y'))

def parsestr2datetime():
    st='2019/06/27 16:25:18'
    dt=datetime.datetime.strptime(st,'%Y/%m/%d %H:%M:%S')
    print(dt)

def takeANap():
    time.sleep(5)
    print('Wake up!!!')

def threaddemo():
    print('Start threading demo.')
    t=threading.Thread(target=takeANap)
    t.start()
    print('main thread stop.')

def threaddemobyargs():
    #print('Cats', 'Dogs', 'Frogs', sep=' & ')
    t=threading.Thread(target=print,args=['Cats', 'Dogs', 'Frogs'],
    kwargs={'sep':' & '})
    t.start()

def startProcess():
    subprocess.Popen('calc')

def startNotepad():
    subprocess.Popen(['notepad','C:\\CollectLog.txt'])

#showdatetime()
#unixtime2datetime()
#beforedate()
#timeDuring()
#threadSleep()
#formatdatetime2str()
#parsestr2datetime()
#threaddemo()
#threaddemobyargs()
#startProcess()
startNotepad()