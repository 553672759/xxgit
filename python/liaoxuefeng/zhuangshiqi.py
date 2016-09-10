#将函数复制给变量，通过变量来调用函数。

#该方法会输出被调用方法的名字
def log(func):
	def wrapper(*args,**kw):
		print('call %s():'%func.__name__)
		return func(*args,**kw)
	return wrapper

#now()方法，加上装饰其log，
#会输出 call now() 相当于执行了now=log(now)
@log
def now():
	print('2016-8-4')



