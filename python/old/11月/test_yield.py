#coding:utf8
'''
Created on 2016-11-23

@author: xx
'''
from _ast import Name

def fab(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1

for n in fab(10):
    print n