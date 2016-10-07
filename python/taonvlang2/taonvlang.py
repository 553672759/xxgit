from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import os
import threading
import re

def main():
	driver=webdriver.PhantomJS(executable_path='C:/Users/xx/xxgit/python/taonvlang/phantomjs-2.1.1-windows/bin/phantomjs')#浏览器的地址
	driver.get("https://mm.taobao.com/search_tstar_model.htm?")#目标网页地址
	bsObj=BeautifulSoup(driver.page_source,"lxml")#解析html语言
	fp=open('mm.txt','r+')#用来将主页的个人信息存储
	fp.write(driver.find_element_by_id('j_GirlsList').text)#获得主页上的姓名、所在城市、身高、体重等信息
	print("[*]OK GET MM's BOOK")
	MMsinfoUrl=bsObj.findAll("a",{"href":re.compile("\/\/.*\.htm\?(userId=)\d*")})#解析出个人主页
	imagesUrl=bsObj.findAll("img",{"data-ks-lazyload":re.compile(".*\.jpg")})#解析出MM的封面图片
	#print(MMsinfoUrl)
	items=fp.readlines()
	content1=[]
	n=0
	m=1
	while (n<14):
		content1.append([items[n].sstrip('\n'),items[m].strip('\n')])
		n+=3
		m+=3
	content2=[]
	for MMsinfoUrl in MMsinfoUrl:
		content2.append(MMsinfoUrl["href"])
	contents=[[a,b] for a,b in zip(content1,content2)]
	i=0
	while(i<5):
		print("[*]MM's name:"+contents[i][0][0]+"with"+contests[i][0][1])
		print("[*]saving......"+contents[i][1])
		path='/photo'+contents[i][0][0]
		mkdir(path)
		getperMMpageImg(perMMpageUrl,path)
		i+=1
	fp.flush()
	fp.close()
	number=1
	for imageUrl in imagesUrl:
		url="https:"+str(imageUrl["data-ks-lazyload"])
		html=urlopen(url)
		data=html.read()
		fileName='/photo/mm'+str(number)+'.jpg'
		fph=open(fileName,"wb")
		print("[+]Loadinging MM.........."+fileName)
		fph.write(data)
		fph.flush()
		fph.close()
		number+=1
	friver.close()
def mkdir(path):
	isExists=os.path.exists(path)
	if not isExists:
		print("[*]新建了一个名字叫做"+path+"的文件夹")
		os.mkdirs(path)
	else:
		print("[+]名为"+path+'的文件夹已经创建成功')

def getperMMpageImag(MMURL,MMpath):
	owndriver=webdriver.PhantomJs(executable_path='C:/Users/xx/xxgit/python/taonvlang/phantomjs-2.1.1-windows/bin/phantomjs')
	owndriver.get(MMURL)
	print("[*]Opening...MM..............")
	ownObj=BeautifulSoup(owndriver.page_source,"lxml")
	perMMings=ownObj.findAll("img",{"ser":re.compile(".*\.jpg")})
	number=2
	for perMMimg in perMMings:
		ImgPath="http:"+str(perMMing["src"])
		try:
			html=urlopen(ImgPath)
			data=html.read()
			fileName=MMpath+"/"+str(number)+'.jpg'
			fp=open(fileName,'wb')
			print("[+]Loading......ger photo ad"+fileName)
			fp.write(data)
			fp.close()
			fp.flush()
			number+=1
		except Exception:
			path("[!]Address Error!!!!!!!!!!!!!!!!!!!")

if __name__=='__main__':
	main()