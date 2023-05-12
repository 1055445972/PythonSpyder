# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 15:23:28 2023

@author: lee‘
"""


#1.build_opener()修改报头
import urllib.request
url="https://img08.tooopen.com/20230408/tooopen_tp_16380838856060.jpg"
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read()
#写入文件
fhandle=open("D:/paquhtml/3.html","wb")
fhandle.write(data)
fhandle.close()