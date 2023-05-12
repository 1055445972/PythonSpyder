# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:40:55 2023

@author: lee‘
"""

#导入urllib库，urllib库下面的reques模块
import urllib.request
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)
#除了write(),urllib.request.urlretrieve()方法可以直接将网页写入本地
#该方法也是必须要对应文件夹
#该方法有局限性，无法设置模拟电脑请求头
urllib.request.urlretrieve("https://img08.tooopen.com/20230408/tooopen_tp_16380838856060.jpg",filename="D:/paquhtml/1.jpg")

#清除urlretrieve()缓存
urllib.request.urlcleanup()