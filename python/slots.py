#动态语言可以在 运行过程中给类加上功能，即给类绑定方法
#但我们不想随便绑定，则用__slots__限制所绑定的方法

class Student(object):
	__slots__=('name','age')

s=Student()
s.name='Eric'
s.age=22
#下面这句会报错，因为slots中没有这个属性
s.score=99

