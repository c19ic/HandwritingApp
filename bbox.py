'''
Function to draw red colour bounding box around character blobs.
1 parameter. Takes in image file path. 
Restrictions to fix:
! Does not consider the moment of characters.
! Does not denoise background of image. 
! Assumes uniform background color and lighting.
~ Line 43: figure size is hard coded. May not be optimal.
~ Line 47: character blob size paramenters is hard coded. Can be optimized.
'''

# Import necessary functions from scikit-image library
from skimage.io import imread, imshow, show
from skimage.transform import resize
from skimage.morphology import square, closing
from skimage.color import rgb2gray
from skimage.measure import label, regionprops
from skimage.segmentation import clear_border
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from skimage.filters import threshold_otsu
from skimage.filters import threshold_adaptive
from matplotlib.cm import binary
from skimage import restoration
from skimage.segmentation import slic
import numpy as np
import math
from skimage.util import invert
from skimage import measure

def drawBBOX(filename='/Users/ishachirimar/noteshrink/HELLOWORLD.jpg'):
    # Read in image, resize, and convert to greyscale
    im = imread(filename) #reading in the image, converts into array
    imshow(im)
    im = resize(im, (500,500)) #resizes array to desired size
    imshow(im)
    
    im = rgb2gray(im) #covnerts 0-255 values to 0-1
    
    # Binarize image to black and white (black background with white blobs)
    thresh = threshold_otsu(im) #chooses optimal # for picture to threshold
    
    bw = im < thresh #takes any value below threshold and makes it white
    # Morphological closing on binary image to fill in gaps (puts ones in place of 0 where hole exists)
    im_close = closing(bw, square(4))
    imshow(im_close)
    # Label connected regions in the image array 
    label_img = label(im_close, neighbors=8, background=0, return_num=False, connectivity=2) #recognizes a region (letter), colors
   #clear objects connected to the label image border
    clean_border = clear_border(label_img) 
    m
    #finds contours of blobs
    contours = measure.find_contours(label_img, 0.8)
    fig, ax = plt.subplots()
    ax.imshow(label_img, interpolation='nearest', cmap=plt.cm.gray)

   
    # Set up plot to prepare image with bbox
    fig, ax = plt.subplots(figsize=(10, 5)) #matlab function, creates empty plot
    ax.imshow(bw) #shows black and white image on plot
    
    #calculate area of blobs
    
    rps = regionprops(clean_border, cache=False)
    #area2 = [r.area for r in rps]
    #find mean of areas
    #mean = np.mean(area2)
   # min12 = mean - (0.15 * mean)
   # max12 = mean + (0.15 * mean)
   
    # Character blob size parameters interested in
    #min_height, max_height, min_width, max_width = (math.sqrt(min12), math.sqrt(max12), math.sqrt(min12), math.sqrt(max12))
    heights = []
    widths = []
    
    #find all heights and widths and append to an array
    for region in rps:
             min_row, min_col, max_row, max_col = region.bbox
             region_height = max_row - min_row
             region_width = max_col - min_col
             heights.append(region_height)
             widths.append(region_width)
    
    median_height = np.median(heights)
    #print "median height", np.median(heights), "median width", np.median(widths), "min height", min(heights), "max height", max(heights), "min width", min(widths), " max width", max(widths)
  
    median_width = np.median(widths)
   
    maxheight = max(heights)
    minheight = min(heights)
    diffheights = maxheight - minheight
    minwidth = min(widths)
    maxwidth = max(widths)
    diffwidths = maxwidth - minwidth
   # print(diffheights, "diff")
    
   #conditions for minimum and maximum
    if diffheights > maxheight/2:
            min_height = np.mean([maxheight, minheight])*0.5
            max_height = maxheight * 10
    
    #print "diffwidth", diffwidths
    if diffwidths > maxwidth/1.2:
            min_width = minwidth/4
            max_width = maxwidth *4
            
    
    
        
            
    #min_height = median_height * 0.2
    #min_height = min(heights)*3
    #max_height = median_height *2.8
    max_height = max(heights) * 2
    #min_width = median_width *0.2
    min_width = min(widths)/5
    #max_width = median_width *2.8
    max_width = max(widths) * 4
    print "min_height", min_height, "max_height",  max_height, "min_width", min_width, "max_width", max_width
    # Counter for number of character blobs in image
    index = 0
    
    # For each character blob in the cleaned border labelled image
#    for region in regionprops(clean_border):
    for region in rps:
        index = index + 1
        
        # pixels to the bounding box region
        min_row, min_col, max_row, max_col = region.bbox
        
        x = min_row
        y = min_col
        w = max_row
        h = max_col
        
        # calculate height and width from returned values from region.bbox
    
        region_height = max_row - min_row
        region_width = max_col - min_col
        
       # region_area = region_height * region_width
        # If the character blob meets these requirements, then draw rectangle shape
#        
        if region_height > min_height and region_height < max_height and \
        region_width > min_width and region_width < max_width:
 #       if region_height > 8 and region_height < 500 and \
 #       region_width > 8 and region_width < 500:
                  
            # Specify the region of interest
            roi = bw[x:w, y:h]
            
            # Draw bounding box around region of interest
            rect_border = mpatches.Rectangle((y, x), h - y, w - x, edgecolor="red",
                                           linewidth=2, fill=False)
    
            ax.add_patch(rect_border)
            
            # Save each bounding box to a .png file with white background black blobs
            plt.imsave('isha'+str(index)+".png", roi, cmap=binary)
    
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()
    
    print "Done."

drawBBOX()