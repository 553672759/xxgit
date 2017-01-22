#coding:utf-8
'''
Created on 2016-11-4

@author: xx
'''
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd
today=date.today()
start=(today.year-1,today.month,today.day)
quotes=quotes_historical_yahoo_ochl('BABA', start, today)
#print df

#对得到的数据进行处理
fields=['date','open','close','high','low','volume']
quotesdf=pd.DataFrame(quotes,columns=fields)
print #print df

#对得到的数据进行处理
fields=['date','open','close','high','low','volume']
quotesdf=pd.DataFrame(quotes,columns=fields)
#print quotesdf[u'2015-12-02':u'2015-12-06']
#转换时间格式
list1=[]
for i in range(0,len(quotes)):
    x=date.fromordinal(int(quotes[i][0]))#遍历数组,取出时间
    y=datetime.strftime(x,"%Y-%m-%d")#将时间格式化为YYYY-MM-DD格式
    list1.append(y)#将格式化的时间放入list1数组里
quotesdf=pd.DataFrame(quotes,index=list1,columns=fields)#利用pandas模块整理数据,以list1数组为index
quotesdf=quotesdf.drop(['date'],axis=1)
#统计某段时间的开盘天数
t=quotesdf[(quotesdf.index>='2016-01-01')&(quotesdf.index<='2016-12-31')]
print len(t)
print quotesdf.sort('close')#根据close这一列进行排序

#
#jiang liang zhang biao jin xing guan lian 
#join
#pd.merge(djidf,akdf,on='code')




