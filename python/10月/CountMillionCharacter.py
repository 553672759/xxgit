# coding:utf8
#统计字符串
'''
Created on 2016-10-17

@author: xx
'''


import pprint

var='''adfsadfsava
sva/sd.,c'qokr210
98102ptk87124312--=`1.2gokvjuncx'[
'''
count={}
for character in var.upper():
    count.setdefault(character,0)
    count[character]=count[character]+1

value=pprint.pformat(count)
print value