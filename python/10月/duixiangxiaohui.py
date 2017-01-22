# coding:utf8
#对象销毁

'''
python与java一样用'引用记数'来追踪内存中的对象。
python内部记录这所有使用种的对象各有多少引用。
一个内部跟踪变量，成为一个引用记数器。
当对象被创建时，就创建了一个引用计数器，当这个对象引用记数变为0时
解释器会在适当时机回收该对象内存空间。

python垃圾收集器：引用计数器+循环垃圾收集器
'''

#析构函数__del__

class Point:
	
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	
	def __del__(self):
		class_name=self.__class__.__name__
		print class_name,"销毁"

pt1=Point()
pt2=pt1
pt3=pt1
print id(pt1),id(pt2),id(pt3)#打印对象的id








