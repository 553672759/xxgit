#-*-coding:utf-8-*-
import pymysql
import math
import random
conn=pymysql.Connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='xx',charset='utf8')
cursor=conn.cursor()

'''
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql="""create table employee(
        id int,
        name char(20)
        )"""
cursor.execute(sql)
'''
num=random.randint(0,999)
print(num)
conn.close()