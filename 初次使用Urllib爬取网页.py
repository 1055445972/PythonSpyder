# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:16:37 2023

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

print(dataline)

print(data)
#网页第一行内容