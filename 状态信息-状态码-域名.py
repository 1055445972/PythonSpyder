# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:44:47 2023

@author: lee‘
"""

#导入urllib库，urllib库下面的reques模块
import urllib.request
#request模块下面的urlopen()方法，打开网页
file=urllib.request.urlopen("http://www.baidu.com")
#read()，读取网页内容

#返回当前环境相关信息，'网页'.info(),前面将网页赋给了file
file.info()

#获取网页状态码,200正确
file.getcode()

#获取当前爬取网页的url
file.geturl()