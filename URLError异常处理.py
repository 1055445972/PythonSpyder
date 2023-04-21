import urllib.request
import urllib.error
try:
    urllib.request.urlopen("http://blog.csdn.net")
    print("can spyder")
except urllib.error.URLError as  e:
    print(e.code)
    print(e.reason)


'''
URLError产生原因
1.连接不上服务器
2.远程URL不存在
3.无网络
4.触发HTTPErro
'''
#如果是第4种原因可以用HTTPError替换URLError
try:
    urllib.request.urlopen("http://blog.csdn.net")
    print("can spyder")
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)

#实际中可以先用子类处理，再用父类处理

try:
    urllib.request.urlopen("http://blog.csdn.net")
    print("can spyder")
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)
except urllib.error.URLError as  e:
    print(e.reason)

#只用URLError类处理，但是有一个问题，当url问题是前3种时是没有状态码
#通过hasattr()来判断是否有该属性
try:
    urllib.request.urlopen("http://blog.csdn.net")
    print("can spyder")
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)

