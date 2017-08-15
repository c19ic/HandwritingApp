import numpy as np
import scipy as scipy

def resize_and_normalize_image(img):  
    
    pad_size = abs(img.shape[0]-img.shape[1]) // 2  
    if img.shape[0] < img.shape[1]:  
        pad_dims = ((pad_size, pad_size), (0, 0))  
    else:  
        pad_dims = ((0, 0), (pad_size, pad_size))  
    img = np.lib.pad(img, pad_dims, mode='constant', constant_values=255)  
    
    # ZOOM
    img = scipy.misc.imresize(img, (64 - 4*2, 64 - 4*2))  
    img = np.lib.pad(img, ((4, 4), (4, 4)), mode='constant', constant_values=255)  
    assert img.shape == (64, 64)  
   
    img = img.flatten()  
    
    # Pixel values range from -1 to 1
    img = (img - 128) / 128  
    return img  

# one hot  
def convert_to_one_hot(char):  
    vector = np.zeros(len(char_set))  
    vector[char_set.index(char)] = 1  
    return vector  

# shuffle sample
train_data_x, train_data_y = shuffle(train_data_x, train_data_y, random_state=0)  
   
batch_size = 128  
num_batch = len(train_data_x) // batch_size  
   
text_data_x = []  
text_data_y = []  
for image, tagcode in read_from_gnt_dir(gnt_dir=test_data_dir):  
    tagcode_unicode = struct.pack('>H', tagcode).decode('gb2312')  
    if tagcode_unicode in char_set:  
        text_data_x.append(resize_and_normalize_image(image))  
        text_data_y.append(convert_to_one_hot(tagcode_unicode))  
	



