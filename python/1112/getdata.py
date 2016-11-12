# coding:utf-8
'''
Created on 2016-11-12

@author: xx
'''
import urllib2, re
dStr = urllib2.urlopen('https://hk.finance.yahoo.com/q/cp?s=%5EDJI').read()
m = re.findall('<tr><td class="yfnc_tabledata1"><b><a href=".*?">(.*?)</a></b></td><td class="yfnc_tabledata1">(.*?)</td>.*?<b>(.*?)</b>.*?</tr>', dStr)
if m:
    print m
    print '\n'
    print len(m)
else:  
    print 'not match'
    

'''
[('AAPL', '\xe8\x98\x8b\xe6\x9e\x9c\xe5\x85\xac\xe5\x8f\xb8', '108.430'),
('AXP', 'American Express Company', '70.500'), 
('BA', 'The Boeing Company', '148.520'),
('CAT', 'Caterpillar Inc.', '93.010'), 
('CSCO', '\xe6\x80\x9d\xe7\xa7\x91\xe7\xb3\xbb\xe7\xb5\xb1\xe5\x85\xac\xe5\x8f\xb8', '31.360'), 
('CVX', 'Chevron Corporation', '106.640'),
('DD', 'E. I. du Pont de Nemours and Company', '69.210'), 
('DIS', 'The Walt Disney Company', '97.680'),
('GE', 'General Electric Company', '30.710'), 
('GS', 'The Goldman Sachs Group, Inc.', '203.940'), 
('HD', 'The Home Depot, Inc.', '129.850'),
('IBM', 'International Business Machines Corporation', '161.270'), 
('INTC', '\xe8\x8b\xb1\xe7\x89\xb9\xe7\x88\xbe\xe5\x85\xac\xe5\x8f\xb8', '34.610'),
('JNJ', 'Johnson &amp; Johnson', '118.470'), 
('JPM', 'JPMorgan Chase &amp; Co.', '76.690'),
('KO', 'The Coca-Cola Company', '41.030'),
('MCD', "McDonald's Corp.", '114.220'), 
('MMM', '3M Company', '175.080'),
('MRK', 'Merck &amp; Co., Inc.', '63.950'),
('MSFT', '\xe5\xbe\xae\xe8\xbb\x9f\xe5\x85\xac\xe5\x8f\xb8', '59.020'),
('NKE', 'NIKE, Inc.', '50.770'), ('PFE', 'Pfizer Inc.', '32.590'),
('PG', 'The Procter &amp; Gamble Company', '83.580'),
('TRV', 'The Travelers Companies, Inc.', '110.280'),
('UNH', 'UnitedHealth Group Incorporated', '146.420'),
('UTX', 'United Technologies Corporation', '108.860'),
('V', 'Visa Inc.', '81.880'),
('VZ', 'Verizon Communications Inc.', '46.690'),
('WMT', 'Wal-Mart Stores Inc.', '71.230'),
('XOM', 'Exxon Mobil Corporation', '85.670')]

'''
