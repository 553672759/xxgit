#coding:utf8
'''
Created on 2017-1-17

@author: xx
题目：暂停一秒输出。
程序分析：无。

'''
import time
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print time.time()
print time.clock()
time.sleep(2)
print time.clock()
