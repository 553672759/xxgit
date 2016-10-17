#conding:utf8
'''
Created on 2016-10-17

@author: xx
'''
import os
try:
    home=os.path.expanduser("~")
    print home
    
    if not os.path.exists(home+'/testdir'):
        os.makedirs(home+'/testdir')
except Exception as e:
        print e
