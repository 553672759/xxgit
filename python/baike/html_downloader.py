# coding:utf8

'''
Created on 2016-10-4

@author: xx
'''
import urllib2


class Html_Downloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        
        response=urllib2.urlopen(url)
        
        if response.getcode()!=200:
            return None
        
        return response.read()
    
    



