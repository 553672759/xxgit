#coding:utf8
'''
Created on 2016-12-28

@author: xx
'''
def swap(ar,j,q):
    a=ar[j]
    ar[j]=ar[q]
    ar[q]=a
    
def ModInsSort(date,n,delta):
    i=delta
    while i<n:
        j=i
        while j>=delta:
            if(date[j]<date[j-delta]):
                swap(date,j,j-delta)
            else:
                break
            