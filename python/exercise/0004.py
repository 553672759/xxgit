#coding:utf8
'''
Created on 2017-1-5

@author: 

第 0004 题：
任一个英文的纯文本文件，
统计其中的单词出现的个数。
'''
import re

def countWords():
    #统计文本中单词的出现次数
    with open('text.txt','r') as file:
        data=file.read()
    
    words=re.compile(r'([a-zA-Z]+)')
    #words是一个re中的对象的实例 
    
    #统计每个单词出现的个数
    dic={}
    for i in words.findall(data):
        if i not in dic:
            dic[i]=1
            #一键值对的方式,单词是键,数量是值
        else:
            dic[i]+=1
            
    #将字典里面的item保存到list中
    numlist=[]
    for k,value in dic.items():
        numlist.append((k,value))
        
    #排序
    numlist.sort(key=lambda t:t[0])
    
    #输出结果
    for i in numlist:
        print(i[0],i[1])
        
if __name__=='__main__':
    countWords()
    
    
    
    
    
    
    
    
    



    