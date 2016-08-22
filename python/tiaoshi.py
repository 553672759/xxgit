#调试程序用 断言 代替 print打印数据
def foo(s):
	n=int(s)

	#表达式n!=0应该是Ture，否则根据程序运行的逻辑，后面的代码肯定出错
	assert n!=0,'n is zero!'

	return 10/n 

def main():
	foo('0')

foo('0')

#解释器可以用 -0来关闭assert
#关闭后可以把assert当成pass

############################
#第三种logging
import logging
logging.basicConfig(level=logging.INFO)

s='0'
n=int(s)
logging.info('n = %d' %n)
print(10/n)

#################
#第四种方式，pdb
#python -m pdb tiaoshi.py
#单行执行，输入n来执行下一行
#可以输入  p 变量名  来查看变量的状态
#输入q结束pdb

#或者设置断点
pdb.set_trace()#程序运行到此会停止