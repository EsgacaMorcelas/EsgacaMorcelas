# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 19:40:01 2021

@author: leogu
"""
import os

coty_folder = 'C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/YOLOv4/coty'
minus9_folder ='C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/YOLOv4/minus9'
plus9_folder = 'C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/YOLOv4/plus9'
ready_folder = 'C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/YOLOv4/ready'
final = 'C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/YOLOv4/dets_together'

coty_ann = os.listdir(coty_folder)
minus9_ann = os.listdir(minus9_folder)
plus9_ann = os.listdir(plus9_folder)
ready_ann = os.listdir(ready_folder)

ann = []

for i in coty_ann:
    ann.append(i)
for j in minus9_ann:
    if j in ann:
        continue
    else:
        ann.append(j)
for k in plus9_ann:
    if k in ann:
        continue
    else:
        ann.append(k)
for l in ready_ann:
    if l in ann:
        continue
    else:
        ann.append(l)

for file in ann:
    together = open(final + '/' + file,'x')
together.close()

together_ann = os.listdir(final)

for filename in together_ann:
    a = ready_folder + '/' + filename
    if os.path.isfile(a):
        e = open(final + '/' + filename,'a')
        with open(a) as infile:
            contents = infile.read()
            e.write(contents)
    e.close()
            
    
