#hashlib
#提供常见的摘要算法
import hashlib
md5=hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
#还可分次调用update，结果是一样的
#MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。

print()
#SHA1
sha1=hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

#在数据库中保存用户口令的时候，存储用户口令的摘要
#用户输入明文口令，然后计算出md5，再和数据库中存储的md5对比

#如果得到MD5口令的数据库，可不必反推，可以对比常用的口令的MD5

#如果想要防止暴力解密简单的md5，可以‘加盐’
def calc_md5(password):
	return get_md5(password+'the-Salt')

#这样，只要the-Salt这个字符串不被其他人知道，即使简单的密码的md5也不会被解密
