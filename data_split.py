#data split
import os, glob
import scipy.misc as misc
import numpy as np
np.random.seed(0)

#where the data is saved
splitDataDir = "/media/ruiyuan/Backup/Yanan/FCN_CRF/"
imagesPath = os.path.join(splitDataDir, "images")
annotationsPath = os.path.join(splitDataDir, "annotations")
if not os.path.exists(imagesPath):os.makedirs(imagesPath)
if not os.path.exists(annotationsPath):os.makedirs(annotationsPath)

#where the data is
dataDir = "/media/ruiyuan/Backup/VOCdevkit/"
scribblePath = os.path.join(dataDir, "scribble", "*."+"png")
scribble_file_list = []
scribble_file_list.extend(glob.glob(scribblePath))
print len(scribble_file_list)
np.random.shuffle(scribble_file_list)

#sperate data
dataLen = len(scribble_file_list)
directories = {"training":scribble_file_list[:0.8*dataLen], "validation":scribble_file_list[0.8*dataLen:0.9dataLen], "testing":scribble_file_list[0.9*dataLen:]}

#main part
for directory in directories.keys():
	print directory

	#create directories
	imagesDirectoryPath = os.path.join(imagesPath, directory)
	annotationsDirectoryPath = os.path.join(annotationsPath, directory)
	if not os.path.exists(imagesDirectoryPath):os.makedirs(imagesDirectoryPath)
	if not os.path.exists(annotationsDirectoryPath):os.makedirs(annotationsDirectoryPath)

	for scribble_file in directories[directory]:
		filename = os.path.splitext(scibble_file.split("/")[-1])[0]
		print scibble_file, filename

		annotation = misc.imread(scibble_file)
		misc.imsave(os.path.join(annotationsDirectoryPath, filename +'.png'), annotation.astype(np.uint8))
		
		image_file = os.path.join(dataDir, "JPEGImages", filename + '.jpg')
		print image_file
		
		if os.path.exists(image_file):
			image = misc.imread(image_file)
			misc.imsave(os.path.join(imagesDirectoryPath, filename+ '.jpg'), image)
		else:
			print("Image file not found for %s - Skipping" % filename)