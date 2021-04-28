# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 20:35:44 2021

@author: leogu
"""
'''this script can resize the all in a folder'''

from PIL import Image
import os, sys

'''the definition of the specific folder is mannualy'''
path = "C:/Users/leogu/PixelCropRobot_Leandro/Dataset/LACSA/Originais//"
dirs = os.listdir(path)

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            #when choosing the new size, take care of the porpotion of your image
            imResize = im.resize((864, 1152), Image.ANTIALIAS)
            print (im, f, e, imResize)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()