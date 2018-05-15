import urllib2

#直接请求
response=urllib2.urlopen('http://www.baidu.com')

#打印返回值
print response.getcode()

#读取内容
cont=response.read()
