#函数

#导入math包
import math

def nop():
	pass
#方法，移动方法
def move(x,y,step,angle=0):
	nx=x+step*math.cos(angle)
	ny=x+step*math.sin(angle)
	return nx,ny

x,y=move(0,0,5,math.pi/6)
#函数返回结果
print(x,y)
#实际的move
print(move(1,1,5,math.pi/6))
print('########')

def power(x,n):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s
#默认函数参数
def power2(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

print("客户端")
print(power2(5))
#默认参数不必须指向不变的值