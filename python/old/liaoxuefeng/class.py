class Student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score

	def print_score(self):
		print('%s:%s'%(self.__name,self.__score))

	def message(self):
		print('%s is a good student'%self.__name)


s=Student('xx',90)#创建一个Student的实例，并让a指向它
s.print_score()#调用刚刚创建实例的方法，打印出信息
s.message()