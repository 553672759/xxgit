'''
Created on 2016-12-28

@author: 
'''
from random import*  
from time import*  
from math import*  
def shell_sort_0(data,n):  
    time=clock()  
    path=int(n/2);  
    while path:  
        i=path  
        while i<n:  
            temp=data[i]  
            j=i-path  
            while j>=0 and temp<data[j]:  
                data[j+path]=data[j]  
                j-=path  
            data[j+path]=temp  
            i+=1  
        path=int(path/2)  
    return clock()-time  
  
def init_data(data,n):  
    for i in range(n):  
        data.append(randint(1,100000))  
          
def make_dlta(dlta,n):  
    t=(int)(log(2*n+1,3))  
    for i in range(t):  
        dlta.append((int)(0.5*(3**(t-i)-1)))  
  
def shell_sort_1(dlta,data,n):  
    time=clock()  
    for path in dlta:  
        i=path  
        while i<n:  
            temp=data[i]  
            j=i-path  
            while j>=0 and temp<data[j]:  
                data[j+path]=data[j]  
                j-=path  
            data[j+path]=temp  
            i+=1  
    return clock()-time  
  
data=[]  
n=eval(input("请输入数据量:"))  
init_data(data,n)  
p=[]  
dlta=[]  
  
p=[i for i in data]  
print("-----------")  
print("time:%lf"%(shell_sort_0(p,n)))  
  
p=[i for i in data]  
make_dlta(dlta,n)  
print("-----------")  
print("time:%lf"%(shell_sort_1(dlta,p,n)))  
  
time=clock()  
p.sort()  
print("time:%lf"%(clock()-time))  