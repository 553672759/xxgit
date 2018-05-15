#/python/mokuai
#-*- coding:utf-8
#这tm是双下划线 __,坑新手

'a test module'

__author__='xx'

import sys

def test():
	args=sys.argv
	if len(args)==1:
			print('Hello,world')
	elif len(args)==2:
		print('Hello,%s!'%args[1])
	else:
		print('Too many arguments!')

if __name__=='__main__':
	test()