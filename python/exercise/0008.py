#coding:utf8
'''
Created on 2017-1-9

@author: 

第 0008 题：一个HTML文件，找出里面的正文。
'''
from HTMLParser import HTMLParser
from re import sub 
'''
re.sub(pattern, repl, string, count=0, flags=0)
参数：
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
'''
from sys import stderr
from traceback import print_exc
import urllib2

class _DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text=[]
        
    def handle_data(self,data):
        text=data.strip()
        if len(text)>0:
            text=sub('[\t\r\n]+',' ',text)
            self.__text.append(text+'')
            
    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')
    
    def handle_startendtag(self,tag,attrs):
        if tag == 'br':
            self.__text.append('\n\n')
            
    def text(self):
        return "".join(self.__text).strip()
        
'''
Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
'''
        
def dehtml(text):
    try:
        parser=_DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.text()
    except:
        print_exc(file=stderr)
        return text
        
if __name__=='__main__':
    url="http://tech.163.com/14/1219/01/ADPT7MTE000915BF.html"
    html=urllib2.urlopen(url)
    html_code=html.read()
    heml_code=sub('<script>(.*?)</script>','',html_code)
    with open('result.txt','w')as f:
        f.write(dehtml(html_code).decode('gbk').encode('utf-8'))    
        
    
        