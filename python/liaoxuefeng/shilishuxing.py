class Student(object):
	#定义类属性
	classname='Student'
	def __init__(self,name):
		self.name=name

s=Student('s')
print(s.classname)
print(s.name)

#如果实例属性和类属性同名，实例属性会覆盖掉类属性，
#这是想要调用类属性要类名.属性名