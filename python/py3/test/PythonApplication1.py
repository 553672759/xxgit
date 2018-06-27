import sys

import os
import time

from PIL import Image
import pytesseract
pwd = os.getcwd()

image2 = Image.open("img/yingwen.jpg")
image = Image.open("img/erweima.png")
code = pytesseract.image_to_string(image2)
if(code!=""):    
    print(code)
else:
    print("未识别到任何数据")
    