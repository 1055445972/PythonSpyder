import urllib.request
httphd=urllib.request.HTTPHandler(debuglevel=1)
httpshd=urllib.request.HTTPSHandler(debuglevel=1)
opener=urllib.request.build_opener(httphd,httpshd)
urllib.request.install_opener(opener)
data=urllib.request.urlopen("http://edu.51cto.com")
redata=data.read()
fhandle=open("D:/paquhtml/6.html","wb")
#write()，写入
fhandle.write(redata)
#close()关闭
fhandle.close()