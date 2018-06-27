from pytesseract import *  
from pytesseract import image_to_string  
from PIL import Image  
from PIL import ImageGrab  
  
  

x = 345  
y = 281  
m = 462  
n = 327  
  
k = 54  
 
box = (x,y,m,n)  
img = ImageGrab.grab(box)  
img.save("img/yingwen.jpg")  
#img.show()  
y+=54  
n+=54  
  
#图片
names=["kangkang2.png","kangkang3.png","kangkang4.png","kangkang5.png"]  
for name in names:  
    im = Image.open("img/yingwen.jpg")  
    text = image_to_string(im)  
    print(name+":"+text)  