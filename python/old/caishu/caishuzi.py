# coding:utf8
'''
Created on 2016-10-7

@author: xx
'''
from random import randint

def printNum():
    sInput=raw_input(u"请输入你猜的数组（1-100）")
    
    try:
        nInput=int(sInput)
    except (ValueError,TypeError),diag:
        print str(diag)
        
    if nInput<1 or nInput>100:
        print u"你输入的数字不在范围内，请重新输入"
        return None
    
    return nInput
        
def main():
    nValue=randint(1,100)
    #print nValue
    nInput=printNum()
    
    nTotal=0
    while(nInput!=nValue):
        if(nInput<nValue):
            print u"你猜的数小了"
        elif(nInput>nValue):
            print u"你猜的数大了"
        nTotal+=1
        nInput=printNum()
              
    print "猜对了"
    print "一共猜了%d次"%nTotal
    
    if nTotal<10:
        print "恭喜，超过平均水平"
    else:
        print "遗憾，低于平均水平"   
    
if __name__=="__main__":
    main()   
        
        
        
        
        