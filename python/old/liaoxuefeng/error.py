#python的错误处理机制
#try-except-finally
#就像其他高级语言一样，
#只不过错误类型要记
try:
	print('try...')
	r=10/0
	print('result:',r)
except ZeroDivisionError as e:#除零错误
	print('except:',e)
finally:
	print('finally')
print('END')
#所有的错误类型都继承自BaseException
#可以跨多层去调用。

#记录错误
import logging

def foo(s):
	return 10/int(s)

def bar(s):
	return foo(s)*2

def main():
	try:
		bar(0)
	except Exception as e:
		logging.exception(e)

main()
print('END')


#抛出错误（自定义错误类型）
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()