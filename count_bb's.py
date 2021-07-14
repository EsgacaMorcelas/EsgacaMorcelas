# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 10:44:56 2021

@author: leogu
"""

import os
from PIL import Image, ImageFont, ImageDraw

gt_ann = 'C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/MobileNetv2_640_640/gt_ann_review/gt_review_xmin_ymin_xmax_ymax'
gt_bb = 'C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/MobileNetv2_640_640/gt_bb'
det_ann = 'C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/YOLOv4/dets_together_50'
det_bb = 'C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/YOLOv4/dt_bb'
title_font = ImageFont.truetype('C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/Roboto-Medium.ttf', 35)

grounds = os.listdir(gt_bb)
dets = os.listdir(det_bb)

def truths_number():
    
    list=[]
    for i in grounds:
        list.append(i)
        for filename in list:
            name,h = os.path.splitext(i)
            doc = gt_ann + '/' + name + '.txt'
            img = Image.open(gt_bb + '/' + filename)
        with open(doc) as infile:          
            contents = infile.readlines()
            title_text = str(len(contents))

            edit = ImageDraw.Draw(img)
            edit.text((800,1100), title_text, (255,0,0), font=title_font)
            img.save(gt_bb + '/' + filename)

truths_number()

def detects_number():
    
    list=[]
    for i in dets:
        list.append(i)
        for filename in list:
            name,h = os.path.splitext(i)
            doc = det_ann + '/' + name + '.txt'
            img = Image.open(det_bb + '/' + filename)
        with open(doc) as infile:          
            contents = infile.readlines()
            title_text = str(len(contents))

            edit = ImageDraw.Draw(img)
            edit.text((800,1100), title_text, (255,0,0), font=title_font)
            img.save(det_bb + '/' + filename)

#detects_number()
