# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 21:08:56 2023

@author: lee‘
"""

#timeout超时判断，如果超时就会输出“出现异常”
import urllib.request
for i in range(1,100):
    try:
        file=urllib.request.urlopen("https://www.csdn.net/",timeout=10)
        data=file.read()
        print(len(data))
    except Exception as e:
        print("出现异常-->"+str(e))