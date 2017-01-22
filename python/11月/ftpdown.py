#coding:utf8
'''
Created on 2016-11-2

@author: xx
'''

from ftplib import FTP
import os
def ftp_down(filename):
    ftp=FTP()
    ftp.set_debuglevel(2)
    ftp.connect('192.168.0.1','21')
    ftp.login('admin','admin')
    print ftp.getwelcome()
    
    bufsize=1024
    filename="20120904.rar"
    file_handler=open(filename,'wb').write
    #以写模式在本地打开文件
    ftp.retrbinary('RETR %s'% os.path.basename(filename),file_handler,bufsize)
    ftp.set_debuglevel(0)
    file_handler.close()
    ftp.quit()
    print "ftp down OK"
    
    
    
    
    
    
    
    