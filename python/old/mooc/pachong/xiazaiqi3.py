import urllib2,cookielib

#创建cookie容器
cj=cookielib.CookieJar()

#创建1个opener
opener=urllib2.build_openner(urllib2.HTTPCoolieProcessor(cj))

#给urllib2安装opener
urllib2.install_opener(opener)

使用带有cookie的urllib2访问网页
response=urllib2.urlopen("http://www.baidu.com/
")
