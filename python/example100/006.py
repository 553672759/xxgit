#coding:utf8
'''
Created on 2017-1-16

@author: xx

题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），
又称黄金分割数列，指的是这样一个数列：
0、1、1、2、3、5、8、13、21、34、……。
'''

import time
def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a

def fib2(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

start=time.clock()
print fib(10)
end=time.clock()
print end-start

start=time.clock()
print fib2(10)
end=time.clock()
print end-start




