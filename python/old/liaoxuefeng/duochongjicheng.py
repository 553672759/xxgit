#python 可以多重继承
#可继承的类，被定义为MixIn

#多进程模式的TCP服务
class MyTCPServer(TCPServer,ForkingMixIn):
	pass

#多线程模式的UDP服务
class MyUDPServer(UDPServer,ThreadingMixIn):
	pass
