#coding:utf8
'''
Created on 2016-10-26

@author: xx
'''
#python中的集合
#无序不重复

#可变集合set,不可变集合frozenset
names=['wangdachui','niuyun','wangfang','xiaoyan','niuyun']
nameSet=set(names)#集合种没有重复项
print nameSet
namefrozenset=frozenset(names)
print type(nameSet),type(namefrozenset)
#集合关系运算
aSet=set('sunrise')
bSet=set('sunset')
print aSet&bSet#∩交集
print aSet|bSet#∪并集
print aSet-bSet#-或除,差,a集合里面特有的
print aSet^bSet#差分,不能同时属于两个集合
aSet-=set('sun')
print aSet
#用函数完成以上任务
'''
issubset()
issuperset()

面向可变集合
'''
#clear与discard的区别
cSet=set('sunrise')
cSet.add('!')
cSet.remove('!')
cSet.update('Yeah')
cSet.clear()









