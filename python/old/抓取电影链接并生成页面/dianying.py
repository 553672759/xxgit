# coding:Utf8
'''
Created on 2016-10-6

@author: xx
'''
#import html_downloader
import urllib2,re
import cookielib
from bs4 import BeautifulSoup
from warnings import catch_warnings


class dianyingMain(object):
    
    def __init__(self):
        #self.downloader=html_downloader.Html_Downloader()
        self.datas=[]
        
    def run(self):  
        count=99507
        i=1        
        while count<=99518:
            try:
                print i
                url=mainurl+'i/'.encode('utf8')+str(count)+'.html'.encode('utf8')
                print url
                title,link=self.get_data(url)
                print title,link
                data={}
                data['num']=i
                data['title']=title
                data['link']=link
                self.datas.append(data)
            except:
                print 'This page 404'
            count+=1
            i+=1
        self.output_html(self.datas)
            

    def get_detail(self,url):
        i_headers = {
            "user-agent":" Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome",
        }
        req = urllib2.Request(url, headers=i_headers)
        resp=urllib2.urlopen(req)
        #resp=urllib2.urlopen(url,  headers=i_headers)
        return resp.read()
    
    def get_data(self,url):
        page=self.get_detail(url)
        soup=BeautifulSoup(page,'html.parser',from_encoding='utf-8')
        l=soup.find('td',style="WORD-WRAP: break-word").find("a")
        link=l.get_text()        
        #<div class="title_all"><h1>奔跑吧兄弟-20141010~20141031</h1></div>
        t=soup.find('div',class_="title_all").find('h1')
        title=t.get_text()
        
        return title,link
    
    def output_html(self,datas):
        fout=open('output.html','wb')
        
        fout.write("<html>")
        fout.write('<meta http-equiv="Content-type" content="text/html;charset=utf-8" />')
        fout.write('<head><title>电影</title><script>')
        fout.write('function copyUrl()  {')
        fout.write('var url = document.getElementById("aa").href;')
        fout.write('window.clipboardData.setData("Text",url);')
        fout.write('alert("已复制链接");')
        fout.write(' } </script></head>')
        fout.write("<body>")
        fout.write("<table border='1'>")
        
        for data in datas:
            fout.write("<tr>")
            fout.write("<td>&nbsp;%s&nbsp;</td>"%data['num'])
            fout.write("<td>%s</td>"%data['title'].encode('utf-8'))
            fout.write('<td><a title="ftp链接" href="%s" onclick="copyUrl()">右键复制链接</a></td>'%data['link'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
    
if __name__=="__main__":
    mainurl='http://www.dy2018.com/'.encode('utf8')
    r=dianyingMain()
    r.run()
    
