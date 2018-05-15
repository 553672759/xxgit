#coding:utf8
'''
Created on 2017-1-11

@author: xx

第 0012 题： 敏感词文本文件 filtered_words.txt，
里面的内容 和 0011题一样，当用户输入敏感词语，
则用 星号 * 替换，例如当用户输入「北京是个好城市」，
则变成「**是个好城市」。

'''
import re

def checkwords(ipstr):
    word_list=[]
    with open('filter_words.txt','r') as f:
        for line in f:
            word_list.append(line.strip())
    li=word_list
    for word in word_list:
        l=len(re.findall(r'%s' %(word),ipstr))
        if l>0:
            ipstr=ipstr.replace(word,'***')

    print ipstr

if __name__=="__main__":
    ipstr=raw_input("plase input your string:\n")

    checkwords(ipstr)















        