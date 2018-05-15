# coding:utf8
'''
Created on 2016-10-17

@author: xx
'''
#测试url是否连通
import urllib2
try:
    urllib2.urlopen("http://www.google.com",timeout=2)
    print "working connection"
except urllib2.URLError:
    print "No internet connection"
