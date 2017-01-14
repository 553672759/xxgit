#coding:utf8
'''
Created on 2017-1-5

@author:

第 0005 题：你有一个目录，装了很多照片，
把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

'''
from PIL import Image
import glob
from __builtin__ import file

def reSize(dirPath,sizeX=100,sizeY=100):
    for file in glob.glob(dirPath+'*.jpg'):
        print file
        ori=Image.open(file)
        modi=ori.resize((sizeX,sizeY))

if __name__=='__main__':
    reSize('img/', 300, 200)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    