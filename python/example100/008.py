#coding:utf8
'''
Created on 2017-1-17

@author: xx

题目：输出9*9乘法口诀表。
程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
'''

for i in range(1,10):
    for j in range(1,10):
        if j>i:
            continue
        print "%d*%d=% -3d"%(j,i,i*j),
    print "\n"
    
'''
        print "%d*%d=% -3d"%(j,i,i*j),
% -3d要有空格,使后面的占三位
在字符串中有多个变量是后面是%(i,j,k)

'''
    
