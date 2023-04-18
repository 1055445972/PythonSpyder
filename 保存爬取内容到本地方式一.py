# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:28:44 2023

@author: lee‘
"""
#导入urllib库，urllib库下面的reques模块
import urllib.request
#request模块下面的urlopen()方法，打开网页
file=urllib.request.urlopen("http://www.baidu.com")
#read()，读取网页内容
data=file.read()
#readline()，读取网页一行内容
dataline=file.readline()

#open()打开文件夹，"wb"以二进制方式写入,一定要有文件夹，html文件可以没有，它会自动创建
fhandle=open("D:/paquhtml/1.html","wb")
#write()，写入
fhandle.write(data)
#close()关闭
fhandle.close()
