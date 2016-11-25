#coding:utf-8
'''
Created on 2016-11-21

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
#选择某些行
#print quotesdf[u'2016-10-01':u'2016-10-06']
#选择某列
#print quotesdf['close']
#print quotesdf.open
#loc方法,iloc方法没有尝试成功
#条件筛选
#print quotesdf[quotesdf.index>=u'2016-10-1']
#print quotesdf.loc[u'2016-02-02':u'2016-02-04',['open','close']]
#print quotesdf.loc[u'2016-02-02':u'2016-02-04','open']#上下两者区别是,下面这个没有列名称
print quotesdf.iloc[1:4,[1]]#取头不取尾










