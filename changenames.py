'''with this script you can change the original name of the pictures taken by a smartphone to make an homogeneous dataset'''

from PIL import Image
import os 
import time

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

def changename():
    for s in species:
        for f in folders:
            if s == f:
                c = 0
                diretory = folder + pathsep + f + pathsep + 'raw/' # the folder to inventory
                outputfile	= folder + pathsep + f + pathsep + 'raw.txt' # file to save the results to
                #obtain just the original pictures not the annotated ones
                midlepath = os.listdir(folder + '/' + s + '/' + 'raw')
                for i in midlepath:
                    if i[0] == 'I' and i[1] == 'M' and i[2] == 'G':
                        x = time.ctime(os.path.getctime(diretory+i))
                        #this script only works with the new images, if the picture name is different, the if should be changed
                        a = diretory + i
                        b = diretory + str(f) + '_' + x[4:7] + '_' + x[8:10]
                        d = b.replace(' ','')
                        c+=1 
                        os.rename(a,d + '_' + str(c) + '.jpg')
        with open(outputfile, "w") as txtfile:
                for path,dirs,files in os.walk(diretory):
                    sep = "\n---------- " + path.split(pathsep)[len(path.split(pathsep))-1] + ' raw_images ' + str(len(midlepath)) + " ----------"
                    print (sep)
                    txtfile.write("%s\n" % sep)
                    
                    for fn in sorted(files):
                        if not any(x in fn for x in exclude):
                            filename = os.path.splitext(fn)[0]
                            print (filename)
                            txtfile.write("%s\n" % filename)
    txtfile.close()
changename()


