#itertools
import itertools
#natuals()会创建一个捂脸的迭代器，所以会打印出自然序列，停不下来
natuals=itertools.count(1)
#cycle()会把传入的一个序列无限重复下去
cs=itertools.cycle('ABC')
#repeat()复制把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns=itertools.repeat('A',3)
for n in ns:
	print(n)

#通过takewhile()函数根据条件判断截取有限序列
nns=itertools.takewhile(lambda x:x<=10,natuals)
print(list(nns))

#chain(),可以把一组迭代对象串联起来，形成一个更大的迭代器
print('chain()')
for c in itertools.chain('ABC','XYZ'):
	print(c)
print()

#groupby()吧迭代器中相邻的重复元素挑出来放在一起
for key,group in itertools.groupby('AAABBBCCCAAA'):
	print(key,list(group))


