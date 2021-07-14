# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 22:42:20 2021

@author: leogu
"""

import math
from PIL import Image, ImageDraw

w,h = 864, 1152
xmin,ymin,xmax,ymax = 0, 780, 174, 1150
shape = [(xmin, ymin), (xmax, ymax)]

img = Image.open('C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/groundtruths/JPEGImages/LACSA_Jun_7_187_864_1152.jpg')

img1 = ImageDraw.Draw(img) 
 
img1.rectangle(shape, outline ="red", width = 3)

img.show()
