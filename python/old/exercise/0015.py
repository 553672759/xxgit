#coding:utf8
'''
Created on 2017-1-12

@author: 

第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
请将上述内容写到 city.xls 文件中，如下图所示：

'''

import xlwt
import json
import sys
reload(sys)

sys.setdefaultencoding('utf8')
file=xlwt.Workbook(encoding='utf-8')
table=file.add_sheet('city',cell_overwrite_ok=True)
txt=open('city.txt').read()
json_txt=json.loads(txt)
for x in range(len(json_txt)):
    table.write(x,0,x+1)
    table.write(x,1,json_txt[str(x+1)])
file.save('city.xls')
    











