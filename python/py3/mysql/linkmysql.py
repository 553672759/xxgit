import pymysql
conn=pymysql.Connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='xx',charset='utf8')
cursor=conn.cursor()
print(cursor)