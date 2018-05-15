#coding:utf8
'''
Created on 2017-1-12

@author: xx

'''

import urllib2
import urllib
import os
import re
import uuid
from HTMLParser import HTMLParser
from traceback import print_exc
from sys import stderr
from bs4 import BeautifulSoup
from pandas.io.common import urlopen
from nltk.downloader import download


links=[]

def get_details(url):
    resp=urllib2.urlopen(url)
    return resp.read().decode('utf-8')

def get_image_urls(page_url):
    images_url=[]
    
    html=get_details(page_url)
    soup=BeautifulSoup(html,'html.parser')
    #pages=soup.find('div',id="pages").children
    pages=soup.find('div',id="pages").find_all('a')
    #print pages
    for i in pages:
        link=i.get('href')
        if link in links:
            #print '链接已存在'
            pass
        else:
            #print "添加链接",link
            links.append(link)
   
    re_img=re.compile('<img src=(.*?) ')
    re_head=re.compile('<title>(.*?)</title>')
    items=re.findall(re_img, html)
    title=re.findall(re_head,html)
    images_url+=items
        
    return images_url

#效率低
def save_image(url,f_name):
    try:    
        #print "sava_image"
        if os.path.exists(f_name):
            print "文件已经存在"
            pass
        else:
            print url
            resp=urllib2.urlopen(url,timeout=3)
            page=resp.read()
            #print page
            f=open(f_name,'wb')
            print "f open"
            f.write(page)
            print 'You are saving images......',f_name
            f.close()
    except Exception:
        pass
    
            

def download_image(page_url):
    try:
        print "图片个数:",len(images_url)
        print images_url
        #print "".join(title)
        for i in images_url:
            i=i.replace("\"","")
            n=len(i)
            if n>40:
                file_name=i[n-10:n]
                save_image(i,"img/"+file_name)
            #save_image(i, f_name)

    except Exception,e:
        print e

for i in range(9000,9167):
    url="http://www.meitulu.com/item/%d.html"%i
    print url
    if url not in links:
        links.append("http://www.meitulu.com/item/%d.html"%i)


links.append("http://www.meitulu.com/item/9167.html")
print links
images_url=get_image_urls("http://www.meitulu.com/item/9167.html")
print links
download_image(images_url)
for i in links:
    try:
        print "i======",i
        images_url=get_image_urls(i)
        download_image(images_url)
    except Exception:
        pass

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    