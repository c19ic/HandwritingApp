#from skimage.io import imread, imshow
import scipy
from skimage.color import rgb2gray 
from scipy.misc import imread
import numpy as np

my_image = imread("./by_class/4a/train_4a/train_4a_00000.png") # imread in a image --> array

def resize_and_normalize_image(img):  
    
    # greyscale the image
    img = rgb2gray(img)
    
    # padding to make array into an nxn matrix
    # n is the larger value of width and height values
    pad_size = abs(img.shape[0]-img.shape[1]) 
    if img.shape[0] < img.shape[1]:  
        pad_dims = (pad_size, pad_size)
    else:  
        pad_dims = (0, 0)
    
    img = np.lib.pad(img, pad_dims, mode='constant', constant_values=1)

    # resize
    img = scipy.misc.imresize(img, (28, 28))  
    
    img = img.reshape(1,1,28,28).astype('float32')

    # Pixel values range from 0 to 1
    img = img/255  
    return img  


my_image = resize_and_normalize_image(my_image)
print("===Final============================================")
print(my_image)
