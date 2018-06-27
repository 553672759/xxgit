link = "http://www.czsx.com.cn/sort.asp?AClassID=5&NClassID=2&GClassID=0&Page="
list=["http://www.czsx.com.cn/sort.asp?AClassID=5&NClassID=2&GClassID=0&Page="]
for i in range(19):

    pagelink="http://www.czsx.com.cn/sort.asp?AClassID=5&NClassID=2&GClassID=0&Page="+str(i)
    list.append(pagelink)
    print(list)
    #print(pagelink)

