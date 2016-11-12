#coding:utf8
'''
Created on 2016-11-6

@author: xx
'''
from ftplib import FTP  
      
ftp = FTP()  
timeout = 30  
port = 21  
ftp.connect('192.168.1.188',port,timeout) # 连接FTP服务器  
ftp.login('UserName','888888') # 登录  
print ftp.getwelcome()  # 获得欢迎信息   
