#客户端
#socket
import socket
import time
#创建一个socket
#AF_INET代表了ipv4，
timeout=20
socket.setdefaulttimeout(timeout)
time.sleep(10)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
#80是web服务的标准端口，1024以内的端口是标准服务端口
s.connect(('127.0.0.1',9999))

#发送报文头
s.send(b'GET/HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')
#创建数组存储网页返回的内容
buffer=[]
while True:
	d=s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data=b''.join(buffer)

s.close()

header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('sina.html','wb')as f:
	f.write(html)
