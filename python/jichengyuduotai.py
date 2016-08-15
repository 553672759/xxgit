class block(object):

	def __init__(self,x,y):
		self.x=x
		self.y=y

	def move(self,tx,ty):
		x=tx
		y=ty
		print(x,y)
	def putblock(self,x,y):
		__init__(self,x,y)
		print('该方块放置在%s,%s'%self.x,self.y)

class ironblock(block):
	def change(self):
		print('融化成铁块')

class soilblock(block):
	def change(self):
		print('变成土方块')

#与动态语言的区别，静态语言中如果需要传入animal类型时
#必须传入animil类或者是他的子类，
#而对于动态语言，只需要有调用的那个方法就可以。
