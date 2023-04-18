# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 15:36:00 2023

@author: lee‘
"""
#导入urllib库，urllib库下面的reques模块
import urllib.request

#url不能传中文,':','&'等符号,这些符号使用编码传输的
#url编码quote()
urlq=urllib.request.quote("http://www.sina.com.cn")
print(urlq)
#相对的，编码传输要转成中文等字符要解码
#url解码unquote()
urlu=urllib.request.unquote("http%3A//www.sina.com.cn")
print(urlu)