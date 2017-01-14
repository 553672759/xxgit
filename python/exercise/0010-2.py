#coding:utf8
'''
Created on 2017-1-10

@author: 

第 0010 题：使用 Python 生成类似于图中的字母验证码图片

'''

from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

def rndChar():
    return chr(random.randint(65,90))

#随机颜色
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

#随机颜色2
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width=60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))
font=ImageFont.truetype('times.ttf',36)
draw=ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
        
for t in range(4):
    char=rndChar()
    print char
    draw.text((60*t+10,10),char,font=font,fill=rndColor2())

image=image.filter(ImageFilter.BLUR)
image.save('0010.jpg','jpeg')
print "图片已经生成!"

print "text"
for i in range(1,127):
    print i,
    print chr(i)+' ',
    if i%10==0:
        print "\n"
        
print "\n"

"""print "test2\n"
i=[]
for i in range(0,5):
    n=random.randint(1,35)
    i[n]=i[n]+1
    print n"""

