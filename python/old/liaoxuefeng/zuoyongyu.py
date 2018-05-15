#python用_表示私有变量
#正常的变量名是公开的public 
#特殊变量__name__,__author__双下划线
#非公开变量（private）_xx，__xx，不应该被直接应用
#不应该不代表不能

def _private_1(name):
	return 'Hello,%s'%name

def _private_2(name):
	return 'Hi,%s'%name

#将两个方法通过greeting()封装起来，隐藏函数内部细节
def greeting(name):
	if len(name)>3:
		return _private_1(name)
	else:
		return _private_2(name)
