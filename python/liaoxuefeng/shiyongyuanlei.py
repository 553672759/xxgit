#通过type()创建一个class对象
#需要传递三个参数
#1.class的名称
#2.继承的父类集合，注意Python支持多继承，
#3.class的方法名称与还是绑定，

def fn(self,name='world'):
	print('Hello,%s.'%name)

Hello=type('Hello',(object,),dict(hello=fn))

h=Hello()
h.hello()
print(type(Hello))
print(type(h))

#可以动态的创建类，动态语言本身支持运行期动态创建类

#metaclass，直译为元类，（接口）
#当我们定义了类以后，就可以根据这个类创建出实例，所以
#：先定义类，然会创建实例。
#但我们想创建出类呢？就必须根据metaclass创建出类。
#所以：先定义metaclass，然会创建类

class ListMetaclass(type):
	def __new__(cls,name,bases,attrs):
		attrs['add']=lambda self,value:self.append(value)
		return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass=ListMetaclass):
	pass

