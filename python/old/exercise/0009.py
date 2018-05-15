#coding:utf8
'''
Created on 2017-1-10

@author: 

第 0009 题：一个HTML文件，找出里面的链接。

'''

from HTMLParser import HTMLParser
import urllib2

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links=[]
        
    def handle_starttag(self,tag,attrs):
        if tag=="a":
            if len(attrs)==0: pass
            else:
                for(variable,value)in attrs:
                    if variable=="href":
                        self.links.append(value)
                        
        

if __name__=="__main__":
    #url="http://www.taobao.com"
    #不明原因,找淘宝会出错
    url="https://github.com"
    html=urllib2.urlopen(url)
    html_code=html.read()
    hp=MyHTMLParser()
    hp.feed(html_code)
    hp.close()
    print(hp.links)
    with open('0009-result.txt','w') as f:
        f.write(" ".join(hp.links))