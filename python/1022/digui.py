#coding:utf8
'''
Created on 2016-10-22

@author: xx
'''
def fib(n):
    a,b=0,1
    count=1
    while count<n:
        a,b=b,a+b
        count=count+1
        print a

#递归的方式
#如果以递归的方式执行fib2(100)会卡住,why
#递归的效率并没有循环的效率高,只是看起来简介
def fib2(n):
    if n==0 or n==1:
        return n
    else:
        return(fib2(n-1)+fib2(n-2))

if __name__ == '__main__':
    fib(100)#可以
    print fib2(100)#不可以
