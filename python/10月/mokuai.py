# coding:utf8
#模块
'''
Created on 2016-10-14

@author: xx
'''
#import语句
#import module1,module2...
#搜索路径是解释器先进行搜索的目录列表
#模块只会被导入一次

'''
from...import语句
将模块种的制定部分导入到当前命名空间
只会导入某个模块种的某个部分
'''

'''
定位模块，导入模块的搜索顺序是：
当前目录
shell变量PYTHONPATH下的每个目录
python默认目录
'''

'''
PYTHONPATH变量
set PYTHONPATH=/usr/local/lib/python
'''
'''
dir()可以返回列表中的所有模块
globals()
locals()
reload()

'''
'''
python中的包
包是一个分层次的文件目录结构，它定义了一个由模块及子包，
和子包下的子包等组成python的应用环境
为了能够使用所有函数，需要__init__.py里显示的导入语句
当导入这个包时，包__init__.py中导入的就可以调用了
'''














