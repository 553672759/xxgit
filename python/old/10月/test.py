#coding:utf8
'''
Created on 2016-10-22

@author: xx
'''
#执行以下程序，若输入126和2，则程序的运行结果是哪一个选项？
#答案是11111110
#注意126不是128

n=0
def foo(num,base):
    global n#声明该n是全局变量
    n+=1#此处n是全局变量,如果重新赋值会改变全局变量
#    print num,base#加上这两行就能知道为嘛了
    if(num>=base): 
        foo(num/base , base) 
    print num%base,#加一个,可以控制不换行,有空格
#    print num,base,num%base#加上这两行就能知道为嘛了
numA = input()
numB = input()
foo(numA,numB)