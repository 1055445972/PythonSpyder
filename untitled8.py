# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 21:23:39 2023

@author: lee‘
"""

#通过url传递的请求是get请求
#我们利用搜索引擎的get特性，我们在百度搜索发现url中wd="（我们输入搜索的值）"
#实例：利用爬虫自动实现在百度上搜索关键词
#如果是输入中文需要转码
import urllib.request
keywd="hello"
url="http://www.baidu.com/s?wd="+keywd
req=urllib.request.Request(url)
data=urllib.request.urlopen(req).read()
fhandle=open("D:/paquhtml/4.html","wb")
fhandle.write(data)
fhandle.close()
file=urllib.request.urlopen("https://baike.baidu.com/item/hello/38467?fr=aladdin")
#read()，读取网页内容
data=file.read()

print(data)
fhandle=open("D:/paquhtml/4.html","wb")
fhandle.write(data)
fhandle.close()