#post请求实例
import urllib.request
import urllib.parse
url="http://www.iqianyue.com/mypost/"
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