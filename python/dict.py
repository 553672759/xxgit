#dict=dictionary,其他语言中叫map
#可以快速的查找到对应的值
#list链表越长，查询速度越慢

d={'michael':95,'Bob':90,'Eric':100,'Tracy':99}
print(d)
print(d['Eric'])

#通过in判断key是否存在
print('dict的key区分大小写')
print('eric' in d)
print('判断能否得到某key对应的值，得不到返回设定好的值')
print(d.get('eric',-1))


#要删除一个key
d.pop('Bob')
print(d)

#dict特点
#1.查找和插入的速度极快，不会随着key的增加而变慢
#2.需要占用大量的内存，内存浪费多。
##list正好相反
#dict的key必须是不可变的


########################
#set也是key的集合，但是不可重复，会自动过滤掉重复内容
#并且无序的
s=set([1,2,3])
print(s)

s.add(4)
print(s)

s.remove(2)
print(s)

#看成数学意义上的无序和无重复元素集合
#所以两个set可以做交集和并集
s1=set([1,2,3])
s2=set([2,3,4])
print(s1&s2)
print(s1|s2)

##########################
#不可变对象
a='abc'
print(a)
print(a.replace('a','A'))
print(a)
#其中a是变量，'abc'才是字符串对象！


