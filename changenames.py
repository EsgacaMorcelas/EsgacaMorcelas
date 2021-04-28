# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 20:35:44 2021

@author: leogues
"""
'''with this script you can change the original name of the pictures taken by a smartphone to make an homogeneous dataset'''

import os 

#folder with all the species
folder = ('C:/Users/leogu/PixelCropRobot_Leandro/Dataset')

#EPPO code for each one of them
species = ['BEAVV','LACSA','DAUCS','CORSA','SPQOL','BRSRR','RAPSR','ERUVE']

#the 8 folders, each one for a specie
files = os.listdir(folder)

def changename():
    for s in species:
        c = 0
        for f in files:
            if s == f:
                #obtain just the original pictures not the annotated ones
                midlepath = os.listdir(folder + '/' + s + '/' + 'Originais')
                for i in midlepath:
                    #this script only works with the new images, if the picture name is different, the if should be changed
                    if i[0] == 'I' and i[1] == 'M' and i[2] == 'G':
                        a = folder + '/' + s + '/' + 'Originais' + '/' + i
                        b = folder + '/' + s + '/' +  s + '_' + i[10:12] + '_' + i[8:10]
                        c+=1
                        os.rename(a,b + '_' + str(c) + '.jpg')
changename()


