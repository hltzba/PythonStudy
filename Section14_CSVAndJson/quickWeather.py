# encoding:utf-8
#! python3
# quickWeather.py - 获取天气信息
import requests,json
# 天气接口信息查阅https://www.cnblogs.com/cubeTC/p/3794613.html
url='http://www.weather.com.cn/data/cityinfo/101230101.html'
res=requests.get(url)
res.encoding=res.apparent_encoding
res.raise_for_status()
reldata=json.loads(res.text)
pstr='城市：{0} 天气：{1}'.format(reldata['weatherinfo']['city'],reldata['weatherinfo']['weather'])
print(pstr)
