'''
'''

import re
import urllib.request

def getlink(url):
    #模拟浏览器
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]

    #opener安装全局
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data=str(file.read())

    #根据需求构建好链接表达式
    pat = '(https?://[^\S)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    return link

#要爬取的网页链接
url="http://blog.csdn.net"

#获取对应网页中包含的链接地址
linklist=getlink(url)
#通过for循环遍历
for link in linklist:
    print(link[0])
