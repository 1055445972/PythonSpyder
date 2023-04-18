# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 09:09:03 2023

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


#除了write(),urllib.request.urlretrieve()方法可以直接将网页写入本地
#该方法也是必须要对应文件夹
filename=urllib.request.urlretrieve("http://www.baidu.com",filename="D:/paquhtml/2.html")

#清除urlretrieve()缓存
urllib.request.urlcleanup()

#返回当前环境相关信息，'网页'.info(),前面将网页赋给了file
file.info()

#获取网页状态码,200正确
file.getcode()

#获取当前爬取网页的url
file.geturl()

#url不能传中文,':','&'等符号,这些符号使用编码传输的
#url编码quote()
urllib.request.quote("http://www.sina.com.cn")

#相对的，编码传输要转成中文等字符要解码
#url解码unquote()
urllib.request.unquote("http%3A//www.sina.com.cn")

#当我们用urlopen()打开网页403错误的时候，需要模拟浏览器访问,设置User-Agent信息
#两种方法模拟浏览器访问

#1.build_opener()修改报头
import urllib.request
url="https://blog.csdn.net/OneFlow_Official/article/details/129577447"
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read()

#写入文件
fhandle=open("D:/paquhtml/3.html","wb")
fhandle.write(data)
fhandle.close()

#2.add_header()添加报头
import urllib.request
url="https://blog.csdn.net/OneFlow_Official/article/details/129577447"
req=urllib.request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41")
data=urllib.request.urlopen(req).read()

#写入文件
fhandle=open("D:/paquhtml/3.html","wb")
fhandle.write(data)
fhandle.close()

#访问超时设置,timeout=1是1秒,
#1秒访问非常的快，差的服务器无法作出这么快的响应,一般设置为30s
'''

import urllib.request
for i in range(1,100):
    try:
        file=urllib.request.urlopen("http://yum.iqianyue.com",timeout=1)
        data=file.read()
        print(len(data))
    except Exception as e:
        print("出现异常-->"+str(e))

'''


#通过url传递的请求是get请求
#我们利用搜索引擎的get特性，我们在百度搜索发现url中wd="（我们输入搜索的值）"
#实例：利用爬虫自动实现在百度上搜索关键词
#如果是输入中文需要转码
import urllib.request
url="http://www.baidu.com/s?wd="
key="名画"
key_code=urllib.request.quote(key)
url_all=url+key_code
req=urllib.request.Request(url_all)
data=urllib.request.urlopen(req).read()
fhandle=open("D:/paquhtml/4.html","wb")
fhandle.write(data)
fhandle.close()


'''
post请求实例
import urllib.request
import urllib.parse
url="http://www.oqianyue.com/mypost/"
postdata=urllib.parse.urlencode({
    'name':'ceo@iqianyue.com',
    'pass':'aA123456'
    }).encode('utf-8') #将数据使用urlencode()处理后使用，encode()设置为utf-8编码
req=urllib.request.Request(url,postdata)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41")
data=urllib.request.urlopen(req).read()
fhandle=open("D:/paquhtml/5.html","wb")
fhandle.write(data)
fhandle.close()
'''







