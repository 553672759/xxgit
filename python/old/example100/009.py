#coding:utf8
'''
Created on 2017-1-17

@author: xx
题目：暂停一秒输出。
程序分析：无。
'''
import time
myd={1:'a',2:'b'}
for key in myd.keys():
    print key,myd[key]
    time.sleep(2)

'''
dict.items(myd)
并不知道这个怎么用,会报错s

'''
