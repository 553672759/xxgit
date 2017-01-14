# coding:utf8
'''
Created on 2016-10-5

@author: xx
'''
import urllib2
import re
import os
from multiprocessing.util import is_exiting
import urllib
import sys  

class web_crawler:
    #模块的初始化方法
    def __init__(self):
        self.mainurl='https://mm.taobao.com/json/request_top_list.htm'
         
    #得到页面信息
    def get_page(self,index):
        #在mainurl字符串后面加上page参数，可以换页，充分分析网页
        url=self.mainurl+'?page='+str(index)
        req=urllib2.Request(url)
        resp=urllib2.urlopen(req)
        return resp.read().decode('gbk')
    
    #得到页面细节
    def get_details(self,url):
        resp=urllib2.urlopen(url)
        return resp.read().decode('gbk')
    
    #
    def get_contents(self,index):
        page=self.get_page(index)
        pattern=re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<a class="lady-name.*?user_id=(\d*).*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items=re.findall(pattern,page)
        print "items:",items
        content=[]
        for i in items:
            content.append([i[0],i[1],i[2],i[3],i[4]])
        return content
    
    def get_album_contents(self,user_id):
        main_url='https://mm.taobao.com/self/album/open_album_list.htm?&user_id='+user_id+'&page='
        page_index=1
        album_ids=[]
        album_names=[]
        album_contents={}
        
        while(True):
            url=main_url+str(page_index)
            page=self.get_details(url)
            pattern_ids=re.compile('<a class="mm-first" href=".*?album_id=(\d*).*?"')
            pattern_names=re.compile('\s*(.*?)</a></h4>')
            items_ids=re.findall(pattern_ids, page)
            print "items_ids:",items_ids
            items_names=re.findall(pattern_names,page)
            print "items_names:",items_names
            
            if len(items_ids)==0:
                break
            else:
                page_index+=1
                for i in items_ids:
                    if i not in album_ids:
                        album_ids.append(i)   
                    
            album_names+=items_names
        for n in range(len(album_names)):
            album_contents[album_ids[n]]=album_names[n]
        return album_contents
    
    def get_images_urls(self,user_id,album_id):
        main_url='http://mm.taobao.com/album/json/get_photo_list_tile_data.htm?user_id='+user_id+'&album_id='+album_id+"&page="
        #main_url='https://mm.taobao.com/self/album_photo.htm?user_id='+user_id+'&album_id=10000702574&album_flag=0'
        print "main_url:",main_url
        page_index=1
        images_url=[]
        while(True):
            url=main_url+str(page_index)
            page=self.get_details(url)
            pattern=re.compile('<img src="(.*?)"')
            items=re.findall(pattern,page)
            if len(items)==0:
                break
            else:
                page_index+=1
            images_url+=items
        return images_url
    
    def new_folder(self,path,name):
        os.chdir(path)
        name=name.strip()
        name=name.strip('.')
        is_exists=os.path.exists(name)
        if not is_exists:
            print 'Creating a new folder:',name
            os.makedirs(name)
        else:
            print 'The folder named',name,'exists'
            
        return_path=path+'/'.encode('utf8')+name
        return return_path
    
    def save_images(self,user_id,user_name,album_contents):
        path_user=self.new_folder(path=os.getcwd(), name=user_name)
        
        for album_id in album_contents:
            path_album=self.new_folder(path_user, album_contents[album_id])
            urls=spider.get_images_urls(user_id,album_id)
            for n in range(len(urls)):
                print "保存图片"
                self.save_image('https:'.encode('utf8')+urls[n],path_album+'/'.encode('utf8')+str(n+1)+'.'.encode('utf8')+'jpg')
    
    def save_image(self,url,f_name):
        resp=urllib.urlopen(url)
        page=resp.read()
        f=open(f_name,'wb')
        f.write(page)
        print 'You are saving images......'
        f.close()
        
    def save_all(self,start,end):
        for page_index in range(start,end+1):
            print page_index
            contents=self.get_contents(page_index)
            #print contents
            for i in contents:
                print "i",i[0],i[1],i[2]
                album_contents=self.get_album_contents(i[1])
                self.save_images(i[1],i[2],album_contents)
                
if __name__=='__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    spider=web_crawler()
    spider.save_all(1, 1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    