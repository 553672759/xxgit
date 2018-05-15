def zhuce(name,gender):
	print('name:',name)
	print('gender:',gender)

def zhuce2(name,gender,age=6,city='Beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:'city)

def add_end(L=[]):
	l.append['END']
	return L

def add_end2(L=None):
	if L is None:
		L=[]
	L.append('END')
	return L

#传入一个list
#calc([1,2,3])
def calc(numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
		return sum
#改进版
def calc(*numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
		return sum
#命名关键字参数
def person(name,age,**kw):
	if 'city' in kw:
		#有city参数
		pass
	if 'job' in kw:
		#有job参数
		pass
	print('name:',name,'age:',age,'other:',kw)
#参数组合 必选参数，默认参数，可变参数，命名关键字参数，关键字参数
#*args是可变参数，args接收的是一个tuple
#**kw是关键字参数，kw接收的是一个dict

