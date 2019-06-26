# encoding:utf-8
#! python3
# section14.py - 
import csv,json
def readcsv():
    csvfile=open('D:\\收费系统\\ToNewlandDatas\\291ExportDataToNewland\\ForRoadNet\\RGSTATION.csv',
        'r',encoding='utf-8')
    csvreader=csv.reader(csvfile)
    #csvdata=list(csvreader)
    #print(csvdata)
    i=0
    for row in csvreader:
        i+=1
        if i>10:
            break
        print('Row #'+str(csvreader.line_num)+' '+str(row))

def writecsv():
    csvfile=open('C:\\Temp\\csvdemo.csv','w',newline='')#Windows系统下必须传newline空字符串，否则会有两倍行距
    writer=csv.writer(csvfile)
    writer.writerow(['spam','eggs','bacon','ham'])
    writer.writerow(['午餐肉','鸡蛋','熏猪肉','火腿肉'])
    csvfile.close()
    print('写入完成')

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,\
"felineIQ": null}'
dictOfJsonData={'name': 'Zophie', 'isCat': True, 'miceCaught': 0, 'felineIQ': None}

def readjsonstrToDict():
    jsondataAsDict=json.loads(stringOfJsonData)
    print(jsondataAsDict)

def readjsonstrToStr():
    strdata=json.dumps(dictOfJsonData)
    print(strdata)
#readcsv()
#writecsv()
#readjsonstrToDict()
readjsonstrToStr()