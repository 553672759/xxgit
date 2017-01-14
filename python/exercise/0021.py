# coding:utf8
'''
Created on 2017-1-12

@author: 

第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。

阅读资料 用户密码的存储与 Python 示例

阅读资料 Hashing Strings with Python

阅读资料 Python's safest method to store and retrieve passwords from a database

'''

import os
from hashlib import sha256
from hmac import HMAC

SALT_LENGTH = 8
def encrypt_password(password,salt=None):
    if salt is None:
        salt=os.urandom(SALT_LENGTH)
        print "salt:",salt
    if isinstance(password,unicode):
        password=password.encode('UTF-8')
        print "password:",password
    result=password
    for i in xrange(8):
        result=HMAC(result,salt,sha256).digest()
    return salt+result

def validate_password(hashed,input_password):
    return hashed==encrypt_password(input_password, salt=hashed[:SALT_LENGTH])

password='123456'
encrypt=encrypt_password(password)
print password
print encrypt
print validate_password(encrypt,password)









