from urllib import request
url = 'http://www.baidu.com'
respose=request.urlopen(url,timeout=1) #超过一秒没打开网页就放弃打开
print(respose.read().decode('utf-8'))