# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:30:57 2021

@author: leogu
"""

import os

folder = 'C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/Object-Detection-Metrics/MobileNetv2_640_640/gt_review_xmin_ymin_xmax_ymax'
files = os.listdir(folder)

for file in files:
    a = open(folder + '/' + file, 'rt')
    data = a.read()
    data1 = data.replace('coty', 'lettuce')
    a.close()
    a = open(folder + '/' + file, 'wt')
    a.write(data1)
    a.close()
    