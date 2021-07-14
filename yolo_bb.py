# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 20:33:21 2021

@author: leogu
"""

import os
import math
from PIL import Image, ImageDraw

dt_bb = 'C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/YOLOv4/dt_bb'
dt_images = 'C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/gt_jpg'
dt_ann = 'C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/YOLOv4/dets_together_50'

images = os.listdir(dt_images)
grounds = os.listdir(dt_ann)

def truths():
    
    list=[]
    for i in images:
        list.append(i)
        for filename in list:
            name,h = os.path.splitext(i)
            doc = dt_ann + '/' + name + '.txt'
            with open(doc) as infile:          
                contents = infile.readlines()
                img = Image.open(dt_images + '/' + filename)
                final = dt_bb + '/' + name + '.jpg'
                for ann in range(len(contents)):
                    a = contents[ann]
                    coords = a.split()
                    bbch = str(coords[0])
                    xmin = int(coords[2])
                    ymin = int(coords[3])
                    xmax = int(coords[4])
                    ymax = int(coords[5])
                    rec = [(xmin,ymin),(xmax,ymax)]
                    img1 = ImageDraw.Draw(img)
                    if bbch == 'ready':
                        img1.rectangle(rec,outline= '#84fc06',width=3) #verde
                    if bbch == 'coty':
                        img1.rectangle(rec,outline= '#10f3fb',width=3) #azul
                    if bbch == 'plus9':
                        img1.rectangle(rec,outline= '#83fbd3',width=3) #turquesa
                    if bbch == 'minus9':
                        img1.rectangle(rec,outline= '#edffff',width=3) #branco
            img.save(final)

truths()