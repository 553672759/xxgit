#-*-coding:utf-8-*-
import sys



import time
time1 = time.time()
from PIL import Image
import pytesseract

###########��ֵ���㷨
def binarizing(img,threshold):
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img
image = Image.open("img/erweima.png")

###########ȥ���������㷨
def depoint(img):   #input: gray image
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:
                count = count + 1
            if pixdata[x,y+1] > 245:
                count = count + 1
            if pixdata[x-1,y] > 245:
                count = count + 1
            if pixdata[x+1,y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x,y] = 255
    return img



# ת��Ϊ�Ҷ�ͼ
img = image.convert('L')
# ��ͼƬ��ɶ�ֵͼ��
img1=binarizing(img,190)
# img2=depoint(img1)
img1.show()
code = pytesseract.image_to_string(img1)
print("is:" + str(code))