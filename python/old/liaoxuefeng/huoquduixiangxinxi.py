#利用type()判断内容的类型
print(type(123))
print(type('str'))

import types

#定义一个方法
def fn():
	pass
#打印输出 fn是不是一个方法
#用到了types包中的FunctionType	
print(type(fn)==types.FunctionType)

#isinstance() 某种类型是否是某类的子类
#isinstance(a,Animal)

#获得一个对象的所有属性和方法
print(dir('abc'))

class MyObject(object):
	def __init__(self):
		self.x=9
		self.y=19
	def power(self):
		return self.x*self.x

obj=MyObject()

#判断有没有x属性
print(hasattr(obj,'x'))
print(obj.x)
print(hasattr(obj,'y'))
#判断有没有y属性，如果有就输出
if hasattr(obj,'y'):
	print(getattr(obj,'y'))

#判断与没有power方法，如果有，让p执行obj的power方法
print(hasattr(obj,'power'))
if hasattr(obj,'power'):
	p=getattr(obj,'power')
	


