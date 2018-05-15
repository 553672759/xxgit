#coding:utf8
'''
Created on 2017-1-12

@author: 

第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如

下所示：

<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!--
    学生信息表
    "id" : [名字, 数学, 语文, 英文]
-->
{
    "1" : ["张三", 150, 120, 100],
    "2" : ["李四", 90, 99, 95],
    "3" : ["王五", 60, 66, 68]
}
</students>
</root>

'''

import xlrd
from xml.dom.minidom import Document
from xml.etree.ElementTree import Comment, Element
import json

infos = []
info_file = xlrd.open_workbook('students.xls')
info_table = info_file.sheets()[0]
row_count = info_table.nrows
doc = Document()
root = doc.createElement('root')
doc.appendChild(root)
students = doc.createElement('students')
for row in range(row_count):
    student = doc.createElement('student')
    student.setAttribute('name', info_table.cell(row, 1).value.encode('utf-8'))
    scores = doc.createElement('scores')
    score = doc.createElement('score')
    score.setAttribute('subject', '数学')
    score.appendChild(doc.createTextNode('%d' % info_table.cell(row, 2).value))
    scores.appendChild(score)
    score1 = doc.createElement('score')
    score1.setAttribute('subject', '语文')
    score1.appendChild(doc.createTextNode('%d' % info_table.cell(row, 3).value))
    scores.appendChild(score1)
    score2 = doc.createElement('score')
    score2.setAttribute('subject', '英文')
    score2.appendChild(doc.createTextNode('%d' % info_table.cell(row, 4).value))
    scores.appendChild(score2)
    student.appendChild(scores)
    students.appendChild(student)
root.appendChild(students)
file = open('students.xml','w')
file.write(doc.toprettyxml(indent = ''))
file.close()













