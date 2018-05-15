#coding:UTF8
#继承

'''
基础重载方法：
__init__(self):
__del__(self):
__repr__(self):转化为供解释器读取的形式
__str__(self):将值转化为适合人阅读的形式
 __cmp__(self,x):对象比较
'''
'''
python支持运算符重载？？？
私有属性（以两个下划线开头）不能被实例访问
__private__attrs
类的私有方法（以两个下划线开头）
__private_method


'''


class Parent:
    parentAttr=100
    def __init__(self):
        print "调用父类的构造函数"
        
    def parentMethod(self):
        print '调用父类方法'
    
    def setAttr(self,attr):
        Parent.parentAttr=attr
        
    def getAttr(self):
        print "父类属性：",Parent.parentAttr

class Child(Parent):
    def __init__(self):
        print "调用子类构造方法"
    
    def childMethod(self):
        print "调用子类方法child method"
        
c=Child()
c.childMethod() 
c.parentMethod()
c.setAttr(200)
c.getAttr()       
        
        
        
        
        