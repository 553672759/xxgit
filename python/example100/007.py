#coding:utf8
'''
Created on 2017-1-17

@author: xx
题目：将一个列表的数据复制到另一个列表中。
程序分析：使用列表[:]。
'''

'''
直接用b=a是引用,传址调用,
即a,b都指向同一个列表,指的是同一个东西.
'''
a=[1,2,3]
b=a
print b
b.append(4)
print 'b=',b
print 'a=',a
'''
b=a[:]是复制,传值调用
即将a指向的列表复制一份给b,此时实际有了两个列表
修改列表b的内容不会影响a
'''
a=[1,2,3]
b=a[:]
print b
b.append(4)
print 'b=',b
print 'a=',a