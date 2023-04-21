def use_proxy(proixy_addr,url):
    import urllib.request
    proxy=urllib.request.ProxyHandler({'http':proixy_addr})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode('utf-8')
    return data

proixy_addr="113.108.242.106:8181 "#高匿ip代理
data=use_proxy(proixy_addr,"http://www.baidu.com")
print(len(data))
