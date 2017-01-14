#coding:utf8
'''
Created on 2016-10-22

@author: xx
'''
f=open(r'data.txt')


p1=f.read()#将文件中的信息全部读取,此时文件指针已到文件结尾
#可以利用f.tell()查看文件指针位置
print f.tell()
p2=f.read()#再次读去取时为空
print 'p1='+p1,'p2='+p2
f.close()