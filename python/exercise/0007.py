#coding:utf8
'''
Created on 2017-1-5

@author: 

第 0007 题：有个目录，里面是你自己写过的程序，
统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

'''
import os
import re

class countLines:
    def __init__(self):
        self.comment=0;
        self.codes=0;
        self.blank=0;
        self.fileList=[]
    
    def openDir(self,dirname):
        curdir=os.getcwd();
        curdir=curdir+str(dirname)
        print curdir
        dirlist=os.listdir(curdir)
        checkpy=re.compile(r"\.py$")
        for item in dirlist:
            if checkpy.search(item):
                item="/"+item
                self.count(curdir+item)
                
    def count(self,filename):
        self.comment=0
        self.codes=0
        self.blank=0
        f=file(filename,'r')
        
        patcomment=re.compile(r"^\s*#") #匹配注释行有多少(如果混合的话不算注释行)
        patblank=re.compile(r"^\s+$") #匹配空白行,
        
        for line in f.readlines():
            if patblank.search(line):
                self.blank+=1
            elif patcomment.search(line):
                self.comment+=1
            else:
                self.codes+=1 #不是注释行,不是空白行,则是代码行.
                
        self.fileList.append([filename,self.codes,self.comment,self.blank])
        
        f.close()
        
    def getResult(self):
        return self.fileList
    
if __name__=="__main__":
    countInstance=countLines()
    countInstance.openDir(r"/testDir")
    relist=countInstance.getResult()
    code_num=0
    comment_num=0
    for item in relist:
        print item[0]
        print "code num:",str(item[1])
        code_num+=item[1]
        print "blank num:",str(item[3])
        comment_num+=item[3]
        print "\n"
                
    print '代码行有:',code_num
    print "注释行有:",comment_num
        



















