#coding:utf8
'''
Created on 2017-1-12

@author: 

第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中，如下图所示：

'''

import xlwt
import json
import sys
reload(sys)

sys.setdefaultencoding('utf8')

file =xlwt.Workbook(encoding='utf-8')
table=file.add_sheet('student',cell_overwrite_ok=True)
txt=open('student.txt').read()
json_txt=json.loads(txt)
for x in range(len(json_txt)):
    #print "x",x
    table.write(x,0,x+1)
    for y in range(len(json_txt[str(x+1)])):
        #print "y:",y
        table.write(x,y+1,json_txt[str(x+1)][y])
file.save('students.xls')







