#collections是Python内建的集合模块
#其中有很多类

#namedtuple
#用于创建自定义的tuple对象，并规定了tuple元素的个数
#并可以用属性而不是索引来引用tuple的某个元素
from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print('打印左边p的值')
print(p.x)
print(p.y)
print()
print(isinstance(p,Point))
print(isinstance(p,tuple))
#还可定义一个圆类
Circle=namedtuple('Circle',['x','y','r'])

#deque
#deque是为了高效实现插入和删除操作的双向列表，队列和栈
from collections import deque
q=deque(['a','b','c'])
q.append('x')
#添加到左侧
q.appendleft('y')
print(q)
print()

#defaultdict
from collections import defaultdict
dd=defaultdict(lambda:'N/A')
dd['key1']='abc'
print(dd['key1'])#当key1存在时输出
print(dd['key2'])#因为上面修改了默认值，
#所以key2不存在时不会报错KeyError，就输入默认的值
print()

#OrderedDict
from collections import OrderedDict
d=dict([('a',1),('b',2),('c',3)])
print(d)#dict显示是没有顺序的，每次都会变
od=OrderedDict([('a',1),('b',2),('c',3)])
print(od)#会按照插入顺序返回
print()

#Counter
#简单的计数器，
from collections import Counter
print('统计单词中每个字符出现次数')
c=Counter()
for ch in 'programming':
	c[ch]=c[ch]+1
print(c)