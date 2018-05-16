import urllib3
import datetime
#import BeautifulSoup
from bs4 import BeautifulSoup
import re
from urllib import request
import os


#由于不是下载的压缩包格式,需要从前一个页面获取文件名.
# http://tiku.gaokao.com/detail/14847
#下载页面链接如下
# http://tiku.gaokao.com/download/type6/id14847
class daylys(object):
    def __init__(self):
        self.time=datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
        self.user_agents=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36']
        self.headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
    #目前该方法可以模拟浏览器来访问大多数网页
    #参数url为地址，例如https://www.baidu.com/
    def get_page(self,url):
        try:
            urllib3.disable_warnings()
            http=urllib3.PoolManager()
            response = http.request('get',url)
            data=response.data
            fout = open("初中数学.html", "wb")
            time=self.time.encode()
            fout.write(time)
            fout.write(data)
            fout.close()
            page=data.decode('gb2312')
        except Exception as e:
            print(e)
        else:
            return page
    def read_page(self,filename):
        f=open("初中数学.html",'r')
        page=f.read()
        return page

    def get_bs(self,page):
        bspage=BeautifulSoup(page,'html.parser')
        return bspage

    #该方法,输入网站,将得到的链接输出到downlist文件中
    def analysis(self,soup):
        print('start...')
        f = open("downlink.txt", "a+")
        for i in soup.select(".date"):
            linktext=i.text
            linknum=re.findall(r"[[0-9]\d*",i['href'])[0]
            link="http://www.czsx.com.cn/downloadcheck.asp?id="+linknum
            #print(link)
            #以键值对的方式存在txt里,然后再以键值对的方式取出
            #data={"num":linknum,"link":link}

            f.write(link+"\n")

        f.close()
        print('写入完成.')

if __name__=="__main__":
    if os.path.exists("downlink.txt"):
        print('文件已经存在,首先删除')
        os.remove("downlink.txt")
        print('文件删除成功')
    pagelist=["http://www.czsx.com.cn/sort.asp?AClassID=5&NClassID=1&GClassID=13",
              "http://www.czsx.com.cn/sort.asp?AClassID=5&NClassID=1&GClassID=13&Page=2",
              "http://www.czsx.com.cn/sort.asp?AClassID=5&NClassID=1&GClassID=13&Page=3",
              "http://www.czsx.com.cn/sort.asp?AClassID=5&NClassID=1&GClassID=13&Page=4",
              "http://www.czsx.com.cn/sort.asp?AClassID=5&NClassID=1&GClassID=13&Page=5",
              "http://www.czsx.com.cn/sort.asp?AClassID=5&NClassID=1&GClassID=13&Page=6",
              "http://www.czsx.com.cn/sort.asp?AClassID=5&NClassID=1&GClassID=13&Page=7",
              "http://www.czsx.com.cn/sort.asp?AClassID=5&NClassID=1&GClassID=13&Page=8",
              ]
    pagelist2=["http://www.czsx.com.cn/sort.asp?AClassID=5&NClassID=1&GClassID=4",
               "http://www.czsx.com.cn/sort.asp?AClassID=5&NClassID=1&GClassID=4&Page=2",
               "http://www.czsx.com.cn/sort.asp?AClassID=5&NClassID=1&GClassID=4&Page=3",
               "http://www.czsx.com.cn/sort.asp?AClassID=5&NClassID=1&GClassID=4&Page=4",
               "http://www.czsx.com.cn/sort.asp?AClassID=5&NClassID=1&GClassID=4&Page=5"]

    list = ["http://www.czsx.com.cn/sort.asp?AClassID=5&NClassID=10&GClassID=0"]
    for i in range(6):
        pagelink = "http://www.czsx.com.cn/sort.asp?AClassID=5&NClassID=10&GClassID=0" + str(i)
        list.append(pagelink)
        print(list)



#下载网页,写入文件
    day = daylys()
    for i in list:
        day.get_page(i)
        print("网页下载完成")
        # 读取文件,让bs4分析
        page = day.read_page("初中数学.html")
        # print(page)
        bspage = day.get_bs(page)
        print("网页分析完成")
        day.analysis(bspage)

    #读取下载链接的信息
    f=open('downlink.txt',"r")
    num=1
    for i in f:
        filename = "file/%s.rar" % num
        with request.urlopen(i) as web:
            # 为保险起见使用二进制写文件模式，防止编码错误
            with open(filename, 'wb') as outfile:
                outfile.write(web.read())
        print("%s...OK" % num)
        num+=1


