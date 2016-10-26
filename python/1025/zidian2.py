#coding:utf8
'''
Created on 2016-10-25

@author: xx
'''

info={'aaa':3000,'bbb':5000,'ccc':8000}
print info
print info['aaa']#键值查找
info['aaa']=3500#更新
print info
info['ddd']=6500#添加 
print info
print 'fff' in info#判断成员
#del info
#print info

for key in info.keys():
    print 'name=%s,salary=%s'%(key,info[key])
#字典的特殊用法
print "aaa's salary is %(aaa)s."%info

#输出模板
template='''
Welcome to the pay wall.
aaa's salary is %(aaa)s.
bbb's salary is %(bbb)s.
'''
print template%info
#字典的内建函数
print info.keys()#输出键
print info.values()#输出值
print info['eeee']
print info.get('eeee')
#对一个字典增加,修改
aInfo={'wangdachui':3000,'niuyun':2000,'linling':4500}
bInfo={'wangdachui':4000,'niuyun':9999,'wangzi':6000}
aInfo.update(bInfo)
print aInfo
#删除字典
aStock={'AXP':86.40,'ba':122.64}
bStock=aStock#传值复制,
aStock={}
print bStock
aStock={'AXP':86.40,'ba':122.64}
aStock=bStock
aStock.clear()
print "aStock="+aStock
print "bStock="+bStock

'''
字典内建函数
clear()
fromkeys()
get()
has_key()
irems()
keys()
iter()
pop()
setdefault()
update()
values()
...
'''
def func(args1,*argst,**argsd):
    print args1
    print argst
    print argsd
#        位置参数,可变长位置参数,可编程关键字参数
print func('hello,','wangdachui','niuyun','linshuai',a1=1,a2=2,a3=3)





