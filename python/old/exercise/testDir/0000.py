#coding:utf8
'''
Created on 2017-1-5

第 0000 题：
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
类似于微信未读信息数量那种提示效果。 类似于图中效果
'''

from PIL import Image,ImageDraw,ImageFont

def add_text(img,str):
    im=Image.open(img)
    print img,"文件已打开"
    #im.show()#打开图片编辑器

    size=im.size
    fontsize=size[1]/4
    tfont=ImageFont.truetype('times.ttf',50)
    #tfont=ImageFont.load_default().font
    draw =ImageDraw.Draw(im)
    width,height=im.size
    draw.text((width-40,10),str,fill='red',font=tfont)
    im.save('result.jpg','jpeg')
    print "保存成功"
if __name__=='__main__':
    add_text('0000.jpg','91')
    
    
    
    
    
    
    
    
    
    
    
    