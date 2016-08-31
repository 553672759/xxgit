#在python执行对目录操作的命令，可以调用os模块
import os

#查看操作系统类型，分为posix、nt（windows）
print(os.name)
#详细信息(windows系统上没用)
#print(os.uname)
#获取系统中环境变量的值
print(os.environ.get('path'))
#查看当前目录的绝对路径
print(os.path.abspath('.'))
#新建文件夹,首先要表示出完整路径
os.path.join('c:/xxgit/python','testdir')
#或者
os.mkdir('c:/xxgit/python/test2dir')
#删除目录
os.rmdir('c:/xxgit/python/test2dir')

#两个路径合一时，不要直接拼接，通过os.path.join()
#不要求文件真正存在，只是对字符串进行操作
#拆分路径时，通过os.path.split()
print(os.path.split('c:/xxgit/python/xuliehua.py'))

#获得扩展名
print(os.path.splitext('c:/xxgit/python/xuliehua.py'))

#在shutil模块中还有os的补充
#利用python的特性来过滤文件
#列出当前目录下所有目录
print('列出当前目录下所有目录')
print([x for x in os.listdir('.') if os.path.isdir(x)])
print('列出所有.py文件')
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])