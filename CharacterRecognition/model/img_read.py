#from skimage.io import imread, imshow
import scipy 
from scipy.misc import imread
import numpy as np

my_image = imread("./noteshrink/page0000.png") # imread in a image --> array

#imshow(my_image)
# print(my_image)
# print(my_image.shape[0])
# print(my_image.shape[1])
print(my_image.shape)
X_test = np.load('./Handwriting_Local/character_recognition/x_test_data.npy')
print(X_test.shape)


def resize_and_normalize_image(img):  
    
    
    # padding to make array into an nxn matrix
    # n is the larger value of width and height values
    pad_size = abs(img.shape[0]-img.shape[1]) 
    if img.shape[0] < img.shape[1]:  
        #pad_dims = ((pad_size, pad_size),(0, 0))
        pad_dims = (pad_size, pad_size)
    else:  
        #pad_dims = ((0, 0),(pad_size, pad_size))
        pad_dims = (0, 0)
    
    img = np.lib.pad(img, pad_dims, mode='constant', constant_values=255)
    
    # ZOOM
    img = scipy.misc.imresize(img, (28, 28))  
    print(img.shape)
    ##img = np.lib.pad(img, (4, 4), mode='constant', constant_values=255)  
    ## assert img.shape == (64, 64)
    
    
    img = img.flatten()  
    print(img.shape)
    img = img.reshape(img.shape[0],1,28,28).astype('float32')
    print "last: ", img.shape
    """
    # Pixel values range from 0 to 1
    img = img/255  
    """
    return img  

"""   
# reshape to be [samples][pixels][width][height]
my_image = my_image.reshape(my_image.shape[0], 1, 28, 28).astype('float32')
my_image = my_image/255
print (my_image)
"""

print(resize_and_normalize_image(my_image).shape)
