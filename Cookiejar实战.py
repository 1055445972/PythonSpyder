'''
在python3中可以使用Cookiejar库来处理Cookie，python2中可以使用Cookielib处理
cookie和session都能保存会话信息
利用cookie和session就是保持登录状态爬取网址
'''

import urllib.request
import urllib.parse
#   url="http://mooc1-1.chaoxing.com/visit/courselistdata"
url="https://passport.bilibili.com/login?"
postdata=urllib.parse.urlencode({
    'text':'1',
    'password':''
    }).encode('utf-8') #将数据使用urlencode()处理后使用，encode()设置为utf-8编码
req=urllib.request.Request(url,postdata)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41")
data=urllib.request.urlopen(req).read()
fhandle=open("D:/paquhtml/7.html","wb")
fhandle.write(data)
fhandle.close()

url2="https://www.bilibili.com/"
req2=urllib.request.Request(url2,postdata)
req2.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41")
data2=urllib.request.urlopen(req).read()
fhandle=open("D:/paquhtml/8.html","wb")
fhandle.write(data2)
fhandle.close()


'''
我们分析post方法对应的url有两种方法，一种是F12进行分析，另一种是通过Fiddle工具分析

F12分析
1.  一个登录账号的url可能不是真正的登录地址，按F12打开开发者工具，我们在登录界面填好信息点击登录，
    在网络中可以看到很多get请求，只有一个或几个post请求。  
    在post请求中可以看到一个Request URL，这是post真实处理表单的网址

问题是如何才能看出哪个信息是Request URL？要是没有Request URL又如何看post请求地址

2.  在登录界面啊查看网页源代码，找到登录框对应的HTML源代码，根据input标签的name属性来确定提交的数据结构

问题是现在的网址没有name属性，name登录的账号密码是通过什么属性来传递数据的
'''


'''
上面的例子是以登录状态爬取页面
但是当我们爬取第二个页面时，任然需要进行登录。
这时我们需要用cookiejar来保持登录状态爬取页面
步骤思路：
1）导入cookiejar
2）使用http.cookiejar.CookieJar()来创建cookiejar对象
3）使用HTTPCookieProcessor创建cookie处理器，并以其为参数构件opener对象
4）创建全局默认的opener对象
'''

import urllib.request
import urllib.parse
import http.cookiejar
url="post实际登录url"
postdata=urllib.parse.urlencode({
    'text':'1',
    'password':''
    }).encode('utf-8') #将数据使用urlencode()处理后使用，encode()设置为utf-8编码
req=urllib.request.Request(url,postdata)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41")
data=urllib.request.urlopen(req).read()

#   使用http.cookiejar.CookieJar()来创建cookiejar对象
cjar=http.cookiejar.CookieJar()
#   使用HTTPCookieProcessor创建cookie处理器，并以其为参数构件opener对象
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
#   将opener安装为全局
urllib.request.install_opener(opener)
file=opener.open(req)
data=file.read()
file=open("D:/paquhtml/9.html","wb")
file.write(data)
file.close()

url2="以登录状态爬取的网址2"
data2=urllib.request.urlopen(url2).read()
fhandle=open("D:/paquhtml/10.html","wb")
file.write(data2)
file.close()