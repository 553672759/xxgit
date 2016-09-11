#python没有专门处理字节的数据类型
#b'str'可以表示字节

#struct模块
#解决bytes和其他二进制数据类型的转换
import struct
print(struct.pack('>I',10240099))
#>表示字节顺序是big-endian，也就是网络序
#I表示4字节无法好整数
#unpack把bytes编程相应的类型
print(struct.unpack('IH',b'\xf0\xf0\xf0\xf0\x80\x80'))

