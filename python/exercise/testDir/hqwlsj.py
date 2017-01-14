#coding:utf8
'''
Created on 2016-10-22

@author: xx
'''
import urllib2
r=urllib2.urlopen('https://www.amazon.cn')#为什么我不可以直接对http://z.cm打开
html=r.read()
print html