#coding:utf8
'''
Created on 2017-1-12

@author: 


第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

[
    [1, 82, 65535],
    [20, 90, 13],
    [26, 809, 1024]
]
请将上述内容写到 numbers.xls 文件中，如下图所示：
'''
import xlwt
import json
import sys
reload(sys)

sys.setdefaultencoding('utf-8')

file=xlwt.Workbook(encoding='utf-8')
table=file.add_sheet('numbers',cell_overwrite_ok=True)
txt=open('numbers.txt').read()
json_txt=json.loads(txt)
for x in range(len(json_txt)):
    for y in range(len(json_txt[x])):
        table.write(x,y,json_txt[x][y])
file.save('nubmers.xls')
print "转换完成"









