
import scipy
from skimage.color import rgb2gray 
from scipy.misc import imread
import numpy as np
import os, os.path


def resize_and_normalize_image(img_list):  
    ''' img_read() helper function: Resize and normalize each image within the image list
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
    return modified_list

def read_imgs_in_folder(folder_path):
	''' img_read() helper function: Read images in a folder.
		Images can't be in a subfolder.
		Input: path to folder with images to be read
		Output: read images
	'''
	output_images = []
	
	path = folder_path
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
		output_images.append(img)
	return output_images
    
def img_read(folder_path, save_filename):
	''' Reads in images from folder and resizes and normalizes them.
		Saves normalized images as numpy array in data folder.
		Input: folder path
		Output: normalized images
	'''
	read_images = read_imgs_in_folder(folder_path)
	norm_images = resize_and_normalize_image(read_images)
	path = "./data/"
	
	if not os.path.exists(path):
		os.makedirs(path)
		
	if(save_filename.lower().endswith('.npy')):
		save_path = os.path.join(path, save_filename)
		np.save(save_path, norm_images)
		print("Saved %s at %s" % (save_filename, save_path))
	else:
		raise ValueError("Save filename does not end in .npy")
		sys.exit()
	
	return norm_images

## For testing	
#img_read("./test_digit_pics/", "digit_pics.npy")

print("Image resize and normalization done.")
