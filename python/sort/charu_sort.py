#coding:utf8
'''
Created on 2016-12-28

@author: xx
'''
import datetime
import time
from public_function import swap

date=[44,12,36,36,55,10,4,8,6,55,95,24,26]
def insert_sort(date):
    start=time.clock()
    print date
    i=0   
    while i<len(date):
        d=i+1
        while d<len(date):
            if date[i]>date[d]:
                swap(date,i,d)
            d=d+1
        i=i+1            
    print date
    end=time.clock()
    print "run:",end-start

    
        
    
    
    
