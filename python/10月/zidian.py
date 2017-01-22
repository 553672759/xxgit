#coding:utf8
'''
Created on 2016-10-22

@author: xx
'''
'''
字典:一种映射关系
'''
#创建字典的方式
aInfo={'aaa':3000,"bbb":5000}
info=[('aaa',3000),('bbb',5000)]
bInfo=dict(info)
cInfo=dict([('aaa',3000),('bbb',5000)])
dInfo=dict(aaa=3000,bbb=5000)
fInfo=dict((('aaa',3000),('bbb',5000)))
print fInfo
aDict={}.fromkeys(('aaa','bbb','ccc'),8000)#将所有的对应8000
aaDict={}.fromkeys(['aaa','bbb','ccc'],8000)
print sorted(aDict)#输出的是list





