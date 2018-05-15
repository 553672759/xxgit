#coding:utf8
'''
Created on 2017-1-11

@author: 
python 2.7

第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

'''
import os
import re

def filter_word(a):
    f=open('filter_words.txt','r').read()
    if a=='':
        print('Human Rights !')
    elif len(re.findall(r'%s' %(a),f))==0:
        print('Human Rights !')
    else:
        print('Freedom !')
    
z=raw_input('请输入词语:\n')
filter_word(z)