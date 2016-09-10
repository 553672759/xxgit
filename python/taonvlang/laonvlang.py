import os
import threading
import re

def main():
	driver=webdriver.PhantomJs(executable_path='C:/Users/xx/xxgit/python/taonvlang/phantomjs-2.1.1-windows/bin/phantomjs')#浏览器的地址
	driver.get("https://mm.taobao.com/search_tstar_model.htm?")#目标网页地址
	bsObj=BeautifulSoup(driver.page_source,"lxml")#解析html语言
	fp=open('mm.txt','r+')#用来将主页的个人信息存储
	fp.write(driver.find_element_by_id('j_GirlsList').text)#获得主页上的姓名、所在城市、身高、体重等信息
	print("[*]OK GET MM's BOOK")