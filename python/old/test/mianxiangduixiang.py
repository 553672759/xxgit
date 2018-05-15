# coding:utf8
'''
python没有严格的变量类型

'''

"""
三个单引号
三个双引号都可以注释多行
"""

'''
python内置类属性
__dict__:类的属性（包含一个字典，由类的数据属性组成）
__doc__:类的文档字符串
__name__:类名
__module__:类定义所在的模块
（类的全名是'__main__.className',如果类位于一个导入模块mymod中
那么className.__module等于mymod)
'''

class Employee:
    '所有员工的基类'
    empCount=0
    
    #类的构造方法，当创建类的实例的时候被调用
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
        
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount
        #通过类名获取类变量
    
    def displayEmployee(self):
        print "Name:",self.name,",Salary:",self.salary


emp1=Employee("eric",7500)
emp2=Employee("xx",8000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d"%Employee.empCount
#测试类的内置函数
print "Employee.__doc__:",Employee.__doc__
print "Employee.__name__:",Employee.__name__
print "Employee.__module__:",Employee.__module__
print "Employee.__bases__:",Employee.__bases__
print "Employee.__dict__:",Employee.__dict__


