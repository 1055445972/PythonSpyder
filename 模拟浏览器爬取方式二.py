# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 15:33:58 2023

@author: lee‘
"""

#2.add_header()添加报头
import urllib.request
url="https://blog.csdn.net/OneFlow_Official/article/details/129577447"
req=urllib.request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41")
data=urllib.request.urlopen(req).read()
