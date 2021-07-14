# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 14:17:36 2021

@author: leogu
"""

import os

directory = 'C:/Users/leogu/PixelCropRobot_Leandro/train/LACSA/fruitdetect4agrob_lettuce/Evaluation/detections_bb'

[os.rename(os.path.join(directory, f), os.path.join(directory, f).replace('_final', '')) for f in os.listdir(directory)]