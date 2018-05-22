# -*- coding: utf-8 -*-
import os
list=[]
with open("file.txt","r") as f:
    line=  f.readline()
    while line:
        dirname= "name/"+line.strip('\n').decode("utf-8")
        os.makedirs(dirname)
        print"...ok"
        line = f.readline()

