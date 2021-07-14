# -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:18:23 2021

@author: leogu
"""
from PIL import Image
import os, sys

#folder with all the species
folder = ('C:/Users/leogu/PixelCropRobot_Leandro/Dataset')

#EPPO code for each one of them
species = ['BEAVV','BRSRR','CORSA','DAUCS','ERUVE','LACSA','RAPSR','SPQOL']

#the 8 folders, each one for a specie
folders = os.listdir(folder)

def delete_wrongsize():
    for s in species:
        for f in folders:
            if s == f:
                path = folder + '/' + f + '/' + 'raw/'
                dirs = os.listdir(path)
                for item in dirs:
                    im = Image.open(path+item)
                    w,h=im.size
                    im.close()
                    if w*h != 3456*4608:
                        os.remove(path+item)
delete_wrongsize()