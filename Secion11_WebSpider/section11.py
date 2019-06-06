# encoding:utf-8
#! python3
# section11.py
import webbrowser,requests,bs4

def openweb():
    webbrowser.open('https://www.baidu.com')

def downloadActLog():
    res=requests.get('http://localhost:8080/ActLog.txt')
    res.raise_for_status()#raise an exception when request failed.
    print(type(res))    
    print('response code:'+str(res.status_code))
    print('response length:'+str(len(res.text)))
    print('response content:'+res.text[:250])
    #TODO Save file
    actlogfile=open('ActLog.txt','wb')
    for chunk in res.iter_content(100000): # 此处使用迭代写入是为了如果request下载一个比较大的文件时，防止内存消耗太多
        actlogfile.write(chunk)
    actlogfile.close()
    print('ActLog.txt saved.')

def bs4Demo():
    res=requests.get('http://localhost:8080/pyexample.html')
    res.raise_for_status()
    noStarchSoup=bs4.BeautifulSoup(res.text,features='html.parser')
    authorelems=noStarchSoup.select('#author')
    print(str(authorelems))
    print(authorelems[0].getText())
    print(authorelems[0].attrs)

def searchBing(keyword='python'):    
    res=requests.get('http://cn.bing.com/search?q='+keyword)
    res.raise_for_status()
    #print(res.text)
    soup=bs4.BeautifulSoup(res.text,features='html.parser')
    rellinks=soup.select('cite')
    for ele in rellinks:
        print(ele.getText())

#openweb()
#downloadActLog()
#bs4Demo()
searchBing('福建高速')