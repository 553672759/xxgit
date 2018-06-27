# coding=utf-8
import urllib3
import datetime
import ssl
import cookiejar
from bs4 import BeautifulSoup
import socket
from requests.packages.urllib3.exceptions import InsecureRequestWarning


# ssl._create_default_https_context = ssl._create_unverified_context
# url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&ch=&tn=baiduerr&bar=&wd=%E7%83%AD%E7%82%B9"
# user_agents=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36']
# if __name__ == "__main__":
#
#
#     http = urllib3.PoolManager()
#     response = http.request('GET',
#                             url,
#                             headers={
#                                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#                                 'Accept-Language':'zh-CN,zh;q=0.8',
#                                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
#                             })
#     text=response.data.decode('utf-8')
#     print(text)
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
            response = http.request('get',url,self.headers)
            data=response.data
            fout = open("baidu.html", "wb")
            time=self.time.encode()
            fout.write(time)
            fout.write(data)
            fout.close()
            page=data.decode('utf-8')
        except Exception as e:
            print(e)
        else:
            return page
    def get_bs(self,page):
        bspage=BeautifulSoup(page,'html.parser')
        return bspage

if __name__=="__main__":
    #url="https://www.baidu.com/"
    url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=热点"
    day=daylys()
    page=day.get_page(url)
    print("网页下载完成。。。")
    bspage=day.get_bs(page)
    print("网页分析完成。。。")
    # arr_a=bspage.find_all("a")
    # print(arr_a)
    # for i in arr_a:
    #     print(i.get_text())
    print("------------")
    print(bspage.find('a'))



