# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 19:42:20 2021

@author: leogu
"""
import os

folder = 'C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/YOLOv4/dets_together'
together = 'C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/YOLOv4/dets_together_50'

dets = os.listdir(folder)

for file in dets:
    doc = folder + '/' + file
    with open(doc) as infile:
        contents = infile.readlines()
        for ann in range(len(contents)):
            a = contents[ann]
            coords = a.split()
            xfile = open(together + '/' + file, 'a')
            if float(coords[1]) >= 0.50:
                xfile.write(a)
            xfile.close()
                    