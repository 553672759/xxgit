import threading,time
class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
        self.arg=arg
    def run(self):#定义每个线程要运行的函数
        time.sleep(1)
        f=open("test.txt","a+")
        f.write(str(self.arg)+"\n")
        print("%s写入完成"%self.arg)

for i in range(4):
    t =MyThread(i)
    t.start()

print ('main thread end!')