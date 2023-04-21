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