#coding:utf8
'''
Created on 2016-10-30

@author: xx
'''
#便捷的获取数据
from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import pandas as pd
today=date.today()
start = (today.year-1,today.month,today.day)
quotes=quotes_historical_yahoo('AXP',start,today)
df=pd.DataFrame(quotes)
print df    




