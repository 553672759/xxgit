from datetime import datetime,timedelta	
now=datetime.now()
print("当前时间是:")
print(now)
print("时间类型是：")
print(type(now))
#注意datetime是一个模块，datetime模块还包含一个datetime类，
#通过from datetime import datetime才是导入类，
#如果只加 import datetime，则调用类的时候还要加全用
#datetime.teaetime

print("指定某个日期和时间，直接构造")
dt=datetime(2015,4,19,12,20)
print(dt)

#计算机中，时间实际是数字表示的，
#把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time
#记为0（timestamp为0）

#timestamp=0=1970-1-1 00:00:00 UTC+0:00
#把datetime转换成timestamp调用temestamp()
print(dt.timestamp())
#python里的timestamp是浮点数，小数位表示毫秒数
#java与js中的timestamp使用整数表示毫秒数，可以除1000转化

#timestamp转化为datetime
t=dt.timestamp()
print(datetime.fromtimestamp(t))#本地时区时间
print(datetime.utcfromtimestamp(t))#utc时间
#str转换成datetime
cday=datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print(cday)
#datetime转换成str
now=datetime.now()
print(now.strftime('%a,%b %d %H:%M'))
#datetime加减
print(now+timedelta(hours=10))
print(now-timedelta(days=1))

