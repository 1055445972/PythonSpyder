'''
京东商城
给一个url，爬取第一个网页
https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=f6aa050ceaef4ba79e016b2a24b3622f
如何爬取第一页的其他几页呢？观察下一页url的变化，得出结论。用循环老啊爬取接下来的几页
https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&pvid=f6aa050ceaef4ba79e016b2a24b3622f&page=3&s=57&click=0
https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&pvid=f6aa050ceaef4ba79e016b2a24b3622f&page=5&s=116&click=0
这里我们根据浏览可以发现，page=1是第1页，page=3是第2页，在一个页面中往下滑自动加载page=2的信息
            #原来学爬虫的印象：利用某个库，查看html结构，发现 div class="p-img"   后面跟着img连接并且唯一对应
这里需要对整个html进行过滤
特殊标识起始
该特殊标识距离第一个想爬取的图片较近，并且在页面唯一。该特殊标识可以作为有效信息的起始过滤位置
特殊标识结束
该特殊标识距离最后一个想爬取的图片较近，并且在页面唯一。
这里的操作就是把一个大的html先过滤成一个小的html(所需的信息全部包含在小的html中)
https://search.jd.com/Search?keyword=%E6%B8%B8%E6%88%8F%E6%9C%AC&wq=%E6%B8%B8%E6%88%8F%E6%9C%AC&pvid=094d92876b8449169df59ea573d6f89d&page=5
'''

import re
import urllib.request
def craw(url,page):
    url = urllib.request.Request(url)
    url.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41")

    #打开并读取网址
    html1=urllib.request.urlopen(url).read()
    #print(html1)
    #将网址转为字符串
    html1=str(html1)
    #分析html头到html尾-
    pat1='<div id="J_goodsList".+? <div class="page clearfix">'
    #compile()全局匹配字符，findall()源字符
    result1=re.compile(pat1).findall(html1)
    print(type(result1))
    #返回第一个结果
    result1=result1[0]
    #构造提取图片连接正则表达式
    pat2='<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'

    imagelist=re.compile(pat2).findall(result1)
    x=1
    for imageurl in imagelist:
        #保存图片地址 +名字
        imagename="D:/paquhtml/img/"+str(page)+str(x)+".jpg"
        #图片链接
        imageurl="http://"+imageurl
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1
    #爬取第1页到第79页

for i in range(1,5,2):
    #url地址
    url="https://search.jd.com/Search?keyword=%E6%B8%B8%E6%88%8F%E6%9C%AC&wq=%E6%B8%B8%E6%88%8F%E6%9C%AC&pvid=094d92876b8449169df59ea573d6f89d&page="+str(i)
    craw(url,i)