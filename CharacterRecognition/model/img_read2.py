#from skimage.io import imread, imshow
import scipy
from skimage.color import rgb2gray 
from scipy.misc import imread
import numpy as np
import os, os.path


def resize_and_normalize_image(img_list):  
    ''' Resize and normalize each image within the image list
    	Inputs: A list of images
    	Outputs: A list of grey scaled images in shape (input_list_length,1,28,28)
    '''
    modified_list = []
    index = 0;
    for img in img_list:
    	
		# greyscale the image
		img = rgb2gray(img)
	
		# padding to make array into an nxn matrix
		# n is the larger value of width and height values
		pad_size = abs(img.shape[0]-img.shape[1]) 
		if img.shape[0] < img.shape[1]:  
			pad_dims = (pad_size, pad_size)
		else:  
			pad_dims = (0, 0)
	
		img = np.lib.pad(img, pad_dims, mode='constant', constant_values=255)

		# resize
		img = scipy.misc.imresize(img, (28, 28))  
	
		#img = img.reshape(1,1,28,28).astype('float32')

		# Pixel values range from 0 to 1
		img = img/255
		
		modified_list.append(img)
		index = index + 1
	
    modified_list = np.array(modified_list)
    modified_list = modified_list.reshape(len(img_list),1,28,28).astype('float32')
    print(modified_list.shape)
    return modified_list


# ======= For testing ====================================================

output_images = []

path = "./pics/"
#path = raw_input("Input path to directory of images: ")
valid_image = ".png"
for f in os.listdir(path):
    try:
    	ext = os.path.splitext(f)[1]
    	if ext.lower() not in valid_image:
            continue
    	img_path = os.path.join(path,f)	
    except OSError, e:
    	sys.exit()
    img = imread(img_path)
    #img = resize_and_normalize_image(img)
    output_images.append(img)
    
output_images = resize_and_normalize_image(output_images)
    
print(output_images)
print("Image resize and normalize done") 
#my_image = resize_and_normalize_image(my_image)
#print("===Final============================================")
#print(my_image)
