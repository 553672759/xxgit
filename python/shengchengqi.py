print("用list生成")
L=[x*x for x in range(10)]
print(L)
print("用生成器generator生成")
g=(x * x for x in range(10))
for i in g:
	print(i)

print("通过函数循环调用")
def fib(max):
	n,a,b=0,0,1
	while n<max:
		print(b)
		a,b=b,a+b
		n=n+1
	return 'done'
print(fib(6))
#python是通过缩进来识别代码块

print("生成器fib")
def fib2(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n=n+1
	return 'done'
print(fib2(6))

for i in fib2(6):
	print(i)
