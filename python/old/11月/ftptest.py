#coding:utf8
'''
Created on 2016-11-2

@author: xx
'''
from ftplib import FTP
import ftplib
import os

#ftp://a:a@dygod18.com/[%E7%94%B5%E5%BD%B1%E5%A4%A9%E5%A0%82www.dy2018.com]%E8%B6%85%E8%84%9148%E5%B0%8F%E6%97%B6BD%E5%9B%BD%E8%8B%B1%E5%8F%8C%E8%AF%AD%E4%B8%AD%E8%8B%B1%E5%8F%8C%E5%AD%97.mkv

ftp=FTP()
ftp.set_debuglevel(2) 
ftp.connect('202.207.240.119', 21,600)
ftp.login('finalmov','finalmov')
print ftp.getwelcome()


    