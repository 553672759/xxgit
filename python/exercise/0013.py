#coding:utf8
'''
Created on 2017-1-12

@author: 

第 0013 题： 用 Python 写一个爬图片的程序，
爬这个链接里的日本妹子图片 :-)

http://tieba.baidu.com/p/2166231880

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
'''
class _DeHTMLParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.img_links=[]
        
    def handle_starttag(self,tag,attrs):
        if tag=='img':
            try:
                if('pic_type','0') in attrs:
                    for name,value in attrs:
                        if name=='src':
                            self.img_links.append(value)
            except Exception as e:
                print(e)
                
        return self.img_links
    
def dehtml(text):
    try:
        parser=_DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.img_links
    except:
        print_exc(file=stderr)
        return text
        
def main():
    html = urllib2.urlopen('http://tieba.baidu.com/p/2166231880')
    content=html.read()
    print "1=",dehtml(content)
    i=0
    for img_list in dehtml(content):
        img_content=urllib2.urlopen(img_list).read()
        path_name=str(i)+".jpg"
        with open(path_name,'wb')as f:
            f.write(img_content)
        i+=1
if __name__=="__main__":
    main()
        
'''

def get_images(html_url,folder_name,extensions=['gif','jpg','png']):
    request_html=urllib2.Request(html_url)
    try:
        response=urllib2.urlopen(request_html) 
        html=response.read()
        r1=r'<img.+src=\".+?\"'
        r2=r'<img.+src=\"(.+?)\"'
        results=[]
        imgs=[]
        p=re.compile(r1)
        
        for m in p.finditer(html):
            results.append(m.group())
        for result in results:
            compile_result=re.compile(r2)       
            imgs.append(compile_result.sub(r'\1',result))
        
        #判断是否存在该文件夹
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
          
        #将照片的链接一个个的下载    
        for img in imgs:
            #文件名用uuid来命名
            filename=str(uuid.uuid1())
            ex=''
            #通过匹配链接中的后缀选择后缀
            for extension in extensions:
                if '.%s'%extension in img:
                    ex='.%s'%extension
            if ex is '':
                continue
            filename+=ex
            try:
                urllib.urlretrieve('http://imgsrc.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C357%3Bap%3D%C9%BC%B1%BE%D3%D0%C3%C0%B0%C9%2C90%2C365/sign=dea9af356a600c33f079dec02a77327f/f6b6402c11dfa9ec3fd93a3663d0f703908fc185.jpg',os.path.join(folder_name,filename))
                print 'Image save at %s' % filename
            except Exception,ex:
                print ex
    except Exception,e:
        print e
        
#get_images()
get_images(html_url='http://tieba.baidu.com/p/2166231880',folder_name='jp')
                
                
        
        
        
        
        
        
        
        
        
        
         