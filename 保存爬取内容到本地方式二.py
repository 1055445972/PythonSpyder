# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:40:55 2023

@author: lee‘
"""

#导入urllib库，urllib库下面的reques模块
import urllib.request

#除了write(),urllib.request.urlretrieve()方法可以直接将网页写入本地
#该方法也是必须要对应文件夹
filename=urllib.request.urlretrieve("http://www.baidu.com",filename="D:/paquhtml/2.html")

#清除urlretrieve()缓存
urllib.request.urlcleanup()