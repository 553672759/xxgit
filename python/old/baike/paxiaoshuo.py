# coding:utf8
'''
Created on 2016-10-6

@author: xx
'''
import html_downloader,url_manager,html_parser
import urllib2,re
import cookielib
from bs4 import BeautifulSoup
from warnings import catch_warnings



class dianyingMain(object):
    
    def __init__(self):
        self.downloader=html_downloader.Html_Downloader()
        self.url=url_manager.UrlManager()
        self.parser=html_parser.HtmlParser()
        self.datas=[]
        
    def run(self,url): 
        
        self.url.add_new_url(url) 
        while self.url.has_new_url():
            new_url=self.url.get_new_url()
            data=self.downloader.download(new_url)
            print data
            data_text=self.get_data(data)
            

    def get_detail(self,url):
        resp=urllib2.urlopen(url)
        return resp.read().decode('gbk')
    
    def get_data(self,page):
        soup=BeautifulSoup(page,'html.parser',from_encoding='utf-8')
        
        page_text=soup.find('div',id="alltext",class_="clear").find("table").find("tr")
        print page_text.get_text()
        tr=page_text.find_next_siblings()
        for i in tr:
            print i.get_text()
            
        
       

        return page_text
    
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
    mainurl='http://www.kekenet.com/read/201306/245509.shtml'.encode('utf8')
    r=dianyingMain()
    r.run(mainurl)
    
