# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 14:54:20 2021

@author: leogu
"""
import os
import cv2 as cv
from matplotlib import pyplot as plt

grounds = 'C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/MobileNetv2_640_640/gt_bb'
detections = 'C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/MobileNetv2_640_640/dt_bb'
final = 'C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/MobileNetv2_640_640/side_by_side'

images = os.listdir(grounds)
for filename in images:
    image1 = cv.imread(grounds + '/' + filename)
    image2 = cv.imread(detections + '/' + filename) 
    final_frame = cv.hconcat((image1, image2))
    cv.imwrite(final + '/' + filename, final_frame)