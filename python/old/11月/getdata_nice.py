#coding:utf-8
'''
Created on 2016-11-12

@author: xx
'''
#通过雅虎财经接口获得的股票数据
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd
today=date.today()
start=(today.year-1,today.month,today.day)
quotes=quotes_historical_yahoo_ochl('BABA', start, today)
df=pd.DataFrame(quotes)
#print df

#对得到的数据进行处理
fields=['date','open','close','high','low','volume']
quotesdf=pd.DataFrame(quotes,columns=fields)
#print quotesdf

list1=[]
for i in range(0,len(quotes)):
    x=date.fromordinal(int(quotes[i][0]))#遍历数组,取出时间
    y=datetime.strftime(x,"%Y-%m-%d")#将时间格式化为YYYY-MM-DD格式
    list1.append(y)#将格式化的时间放入list1数组里
quotesdf=pd.DataFrame(quotes,index=list1,columns=fields)#利用pandas模块整理数据,以list1数组为index
quotesdf=quotesdf.drop(['date'],axis=1)
print quotesdf









