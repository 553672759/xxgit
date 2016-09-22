#UDP与TCP的区别
#udp协议不需要建立连接，速度快（不稳定)
s=socket.socket(socket.AF_INET,socket>SOCK_DGRAM)
s.bind(('127.0.0.1',9999))

print('Bind UDP on 9999...')
while Thre:
	#接受数据
