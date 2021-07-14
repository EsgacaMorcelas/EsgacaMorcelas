'''this script can resize the all the images in a folder'''

#!/usr/bin/python
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

new_width = 864
new_height = 1152

def resize():
    for s in species:
        for f in folders:
            if s == f:
                new_path = folder + pathsep + f + pathsep + 'resized/'
                outputfile	= folder + pathsep + f + pathsep + 'resized.txt'
                path = folder + pathsep + f + pathsep + 'raw/'
                dirs = os.listdir(path)
                c=0
                for item in dirs:
                    if os.path.isfile(path+item):
                        im = Image.open(path+item)
                        width,height = im.size
                        if width != new_width and height != new_height:
                            imResize = im.resize((new_width,new_height), Image.ANTIALIAS)
                            name_file,e = os.path.splitext(new_path + item)
                            imResize.save(name_file + '_' + str(new_width) + '_' + str(new_height)+'.jpg', 'JPEG', quality=90)
                            c+=1
        
        
        with open(outputfile, "w") as txtfile:
                for path,dirs,files in os.walk(new_path):
                    sep = "\n---------- " + path.split(pathsep)[len(path.split(pathsep))-1] + ' resized_images ' + str(new_width) + '*' + str(new_height) + ' ' + str(c) + " ----------"
                    print (sep)
                    txtfile.write("%s\n" % sep)
                    
                    for fn in sorted(files):
                        if not any(x in fn for x in exclude):
                            filename = os.path.splitext(fn)[0]
                            
                            print (filename)
                            txtfile.write("%s\n" % filename)
        txtfile.close()

resize()
