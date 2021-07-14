# -*- coding: utf-8 -*-
"""
Created on Wed May 26 13:42:24 2021

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

# start editable vars #
exclude		= ['Thumbs.db','.tmp']	# exclude files containing these strings
pathsep		= "/"			# path seperator ('/' for linux, '\' for Windows)
# end editable vars #
def checkfiles():
    final = []
    total_raw = 0
    total_resized = 0
    total_annotated = 0
    for s in species:
        for f in folders:
            if s == f:
                raw = 0
                resized = 0
                annotated = 0
                diretory_raw = folder + pathsep + f + pathsep + 'raw/' # the folder to inventory
                diretory_resized = folder + pathsep + f + pathsep + 'resized/'
                diretory_annotated = folder + pathsep + f + pathsep + 'annotated/Annotations/'
                outputfile	= folder + pathsep + f + pathsep + 'checkfiles.txt' # file to save the results to
                midle_raw = os.listdir(folder + '/' + s + '/' + 'raw')
                midle_resized = os.listdir(folder + '/' + s + '/' + 'resized')
                midle_annotated = os.listdir(folder + '/' + s + '/' + 'annotated/Annotations')
                for i in midle_raw:
                    raw+=1
                for d in midle_resized:
                    resized+=1
                for j in midle_annotated:
                    annotated+=1
                #print(s, 'raw=', raw, 'resized=', resized, 'annotated=', annotated)
        
        with open(outputfile, "w") as txtfile:
            if raw == resized:
                good_job = s + ' raw = ' + str(raw) + ' resized = ' + str(resized) + ' annotated = ' + str(annotated)
                final.append(good_job)
                txtfile.write(good_job)
                total_raw+=raw
                total_resized+=resized
                total_annotated+=annotated
                
    txtfile.close()
    
    total = 'total_raw = ' + str(total_raw) + ' total_resized = ' + str(total_resized) + ' total_annotated = ' + str(total_annotated)
    outputfile2 = folder + pathsep + 'dataset_size.txt'
    with open(outputfile2, 'w') as txtfile:
        for i in range(len(final)):
            txtfile.write('%s\n' % str(final[i]))
        txtfile.write('%s\n' % total)
    txtfile.close()
            

checkfiles()