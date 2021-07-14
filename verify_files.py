# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:49:16 2021

@author: leogu
"""
import os

folder1 = 'C:/Users/leogu/OneDrive/Área de Trabalho/jpg_val_final'
files = os.listdir(folder1)
folder2 = 'C:/Users/leogu/OneDrive/Área de Trabalho/xml_val_final'

for img in files:
    a,b = os.path.splitext(img)
    xml = folder2 + '/' + a + '.xml'
    if os.path.isfile(xml):
        continue
    else:
        print ('Só falta este gambuzino ' + a)