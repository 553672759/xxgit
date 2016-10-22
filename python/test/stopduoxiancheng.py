#http://blog.csdn.net/a464057216/article/details/47678781
#来自上述网站，thinks
#并没有达到预期的效果《按ctrl+c优雅的退出》
import threading,time,signal
import sys
def printA():
	while True:
		print ('a')
		time.sleep(1)

def printB():
	while True:
		print ('b')
		time.sleep(1)

def quit(signum,frame):#3
	print('You choose to stop me.')
	sys.exit()

if __name__=='__main__':
	try:
		signal.signal(signal.SIGINT,quit)#3
		signal.signal(signal.SIGTERM,quit)#3

		a=threading.Thread(target=printA)
		b=threading.Thread(target=printB)
		a.setDaemon(True)#2
		a.start()
		b.setDaemon(True)#2
		b.start()

		#a.join()#1
		#b.join()#1

		while True:#2
			pass
	except Exception(e):
		print (e)