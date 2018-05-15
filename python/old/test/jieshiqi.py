from bs4 import import BeautifulStoneSoup

#根据HTML网页字符串创建BeautifulSoup
soup=BeautifulStoneSoup(
                        html_doc,               #HTML文档字符串
                        'html.parser'           #HTMl解析器
                        from_encoding='utf8'    #HTML文档的编码
                        )   

