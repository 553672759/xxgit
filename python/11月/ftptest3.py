#coding:utf-8
import nltk
from ftplib import FTP
f=FTP('dygod18.com')
f.login('a','a')
print f.getwelcome()  # 获得欢迎s信息
   