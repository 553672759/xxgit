# coding:utf8

'''
Created on 2016-10-4

@author: xx
'''


class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]
    
    def collect_data(self ,data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        fout=open('output.html','wb')
        
        fout.write("<html>")
        fout.write('<meta http-equiv="Content-type" content="text/html;charset=utf-8" />')
        fout.write("<body>")
        fout.write("<table border='1'>")
        
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>"%data['title'].encode('utf-8'))
            fout.write("<td>%s</td>"%data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
    
    
    
    



