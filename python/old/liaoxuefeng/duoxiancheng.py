import time,threading

#新线程执行的代码
def loop():
	print('thread %s is running...' % threading.current_thread().name)
	n=0
	while n<5:
		n=n+1
		print('thread %s >>> %s ' %(threading.current_thread().name,n))
		time.sleep(1)
	print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running ... ' % threading.current_thread().name)
t=threading.Thread(target=loop,name='LoopThrad')
t.start()
t.join()
print('thread %s ended.'%threading.current_thread().name)


#放在另一个文件里
#可以给线程加线程锁
 balance=0
 lock=threading.Lock()
 def run_thread(n):
 	for i in range(100000):
 		#先获取锁
 		lock.acquire()
 		try:
 			#已经加锁，可任意更改
 			change_it(n)
 		finally:
 			#改完释放锁
 			lock.release()