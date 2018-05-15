#coding:utf8
'''
Created on 2016-12-28

@author: xx
python中1~255都是属于整数池里的 ,不可改变,所以没有++/--这样的运算
'''
from public_function import *
from charu_sort import insert_sort
import time

date=[44,12,36,36,55,10,4,8,6,55,95,24,26]

def shell_sort_me(date,n):
    
    start=time.clock()    
    print date
    delta=int(n/2)
    i=0
    while delta>0:
        while i<delta:
            ModInsSort(date[i], n-i, delta)
            i+=1
            
        delta/=2
    print date

def shell_sort(lists):
    count=len(lists)
    step=2
    group=count/step
    while group>0:
        for i in range(0,group):
            j=i+group
            while j<count:
                k=j-group
                key=lists[j]
                while k>=0:
                    if lists[k]>key:
                        print "group:",group," i:",i," j:",j," k:",k
                        lists[k+group]=lists[k]
                        lists[k]=key
                    k-=group
                j+=group
        group/=step
        return lists

print shell_sort(date)