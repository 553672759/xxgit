#coding:utf8
'''
Created on 2017-1-5

@author: 

第 0006 题：你有一个目录，放了你一个月的日记，
都是 txt，为了避免分词的问题，假设内容都是英文，
请统计出你认为每篇日记最重要的词。

'''
import glob
from collections import Counter,OrderedDict

def mostImporantWord(filePath):
    for file in glob.glob(filePath+'*.txt'):
        calcTimes(file)

def calcTimes(fileName):
    cc=Counter()
    file=open(fileName)
    str=file.read()
    words=str.split('\n')
    for i in words:
        cc[i]=cc[i]+1
    maxInDict(cc)
    
def maxInDict(dict):
    max=0
    for key,value in dict.items():
        if value>max:
            max=value
            goal=key
        print goal+"and its time's"+str(max)

if __name__=='__main__':
    mostImporantWord("diaries/")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    