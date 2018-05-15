#coding:UTF8
'''
Created on 2016-10-15
@author: xx

'''
'''
Tkinter编程
是python标准的GUI库
'''
from Tkinter import *

top =Tk()  #初始化
top.title("单词翻译 by_xx")#设置标题
top.geometry('300x200')#设置窗口大小

top.resizable(width=False, height=True)#设置宽不可变，高可变，默认为True
l=Label(top,text="show",bg="green",font=("Arial",12),width=5,height=2)
l.pack(side=TOP)
Label(top,text="1".decode('gbk').encode('utf8'),font=('Arial',20)).pack()

frm=Frame(top) #框架
#left
frm_L=Frame(frm)
Label(frm_L,text='2'.decode('gbk').encode('utf8'),font=('Arial',15)).pack(side=TOP)
Label(frm_L,text='3'.decode('gbk').encode('utf8'),font=('Arial',15)).pack(side=TOP)
frm_L.pack(side=LEFT)

#right
frm_R=Frame(frm)
Label(frm_R,text='4'.decode('gbk').encode('utf8'),font=('Arial',15)).pack(side=TOP)
Label(frm_R,text='5'.decode('gbk').encode('utf8'),font=('Arial',15)).pack(side=TOP)
frm_R.pack(side=RIGHT)

frm.pack()

#单行文本框
var =StringVar()
e=Entry(top,textvariable=var)
var.set('xx')
e.pack()

#多行文本
t=Text(top)
t.insert(1.0, 'hello\n')
t.insert(END,'hello000000\n')
t.insert(END,'nono')
t.pack()

#按钮
Button(top,text="press",relief=FLAT).pack()

#列表控件
def print_item(event):
    print lb.get(lb.curselection()) 

var=StringVar()
lb=Listbox(top,height=5,selectmode=BROWSE,listvariable=var)
lb.bind('<ButtonRelease-1>',print_item)
list_item=[1,2,3,4,5,6,7,8,9,0]
for item in list_item:
    lb.insert(END,item)
scrl=Scrollbar(top)
scrl.pack(side=RIGHT,fill=Y)
lb.configure(yscrollcommand=scrl.set)
lb.pack(side=LEFT,fill=BOTH)
scrl['command']=lb.yview
#进入消息循环
top.mainloop()






