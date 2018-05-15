import urllib.request,http

url="http://www.baidu.com"

print("第一种方法")
response1=urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print('第二种方法')
request=urllib.request.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2=urllib.request.urlopen(request)
print (response2.getcode())
print( len(response2.read()))

print ('第三种方法')
cookie_finename='cookie.txt'
cj=http.cookiejar.MozillaCookieJar(cookie_filename)
handler=urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(handler)
response=urllib.request.urlopen(opener)
print (response3.getcode())
print (len(response3.read()))


#python 3.x中urllib库和urilib2库合并成了urllib库。。
#其中urllib2.urlopen()变成了urllib.request.urlopen()
#urllib2.Request()变成了urllib.request.Request() 
