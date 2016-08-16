class Student(object):
	def __init__(self,name):
		self.name=name

class Student2(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return 'Student object (name:%s)'%self.name
	__repr__=__str__
#__repr__是给开发者看的
#__srt__是给用户看的


print(Student2('Eric'))

#iter该方法返回一个迭代对象，可以让类被用于for...in

class Fib(object):
	def __init__(self):
		self.a,self.b=0,1

	def __iter__(self):
		return self #实例本事就是迭代对象，故返回自己

	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>100000:
			raise StopIteration();
		return self.a #返回下一個值

for n in Fib():
	print(n)

#__getitem__()
#該方法可以使函數像list的方式取值
class Fib2(object):
	def __getitem__(self,n):
		a,b=1,1
		for x in range(n):
			a,b=b,a+b
		return a

	def __getitem__(self,n):
		if isinstance(n,int):#n是索引
			a,b=1,1
			for x in range(n):
				a,b=b,a+b
			return a
		if isinstance(n,slice):n是切片
			start=n.start
			stop=n.stop
			if start is None:
				start=0
			a,b=1,1
			L=[]
			for x in range(stop):
				if x>=start:
					L.append(a)
				a,b=b,a+b
			return L

f=Fib()		
#下標從零開始
print(f[4])
#或者用list的切片
print(f[5:10])

#__getattr__
#调用类的方法或属性时，没有值是会在该方法中找
class Student(object):
	def __getattr__(self,attr):
		if attr=='age':
			return lambda:25

#Chain链式调用，见Chain.py
#__call__直接对实例进行调用
class Student(object):
	def __init__(self,name):
		self.name=name
	def __call__(self):
		print('My name is %s'% self.name)

#调用
s=Student('Michael')
s()