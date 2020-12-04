# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.colors as colors

#Part_1 
img = plt.imread('/Users/torijamaximoj2/Desktop/salience_08.png')
plt.imshow(img) # Image is an array of 99 (height) * 150 (width) * 3 (color channels)
#red = img[:, :, 0]
#green = img[:, :, 1]
#blue = img[:, :, 2]
height, width, channels = img.shape


color = ["red", "green", "blue"]
plt.figure(figsize = (12,7))
plt.subplot(2,2,1) , plt.imshow(img) , plt.title('Original Image')
j = 0
while j < 3 :
    plt.subplot(2,2,j+2)
    plt.imshow(img[:,:,j], cmap = 'gray')
    plt.title(color[j] + ' channel')
    j = j + 1

    
def channel_corr(img):
    width, height, channels = img.shape #properties of image stored into img.shape
    img_vector = np.zeros((channels,width*height)) #np.shape is the shape of new array to store vectors
    #load the channels and corresponding values into one array for width and height
    for i in range(channels):
        img_vector[i,:] = img[:,:,i].flatten()
    return np.corrcoef(img_vector)

#Get the correlation coefficient
img_corr = channel_corr(img)
plt.imshow(img_corr),plt.colorbar()
plt.xticks(range(3), ["Red", "Green", "Blue"]),plt.yticks(range(3), ["Red", "Green", "Blue"])

#Part 2
img_hsv = colors.rgb_to_hsv(img)
print(img_hsv)
plt.figure(figsize = (12,7))
plt.subplot(2,2,1) , plt.imshow(img_hsv) , plt.title('HSV Image')
j = 0
hsv_list = ["Hue", "Saturation", "Value"]
while j < 3 :
    plt.subplot(2,2,j+2)
    plt.imshow(img_hsv[:,:,j], cmap = 'gray')
    plt.title(hsv_list[j] + ' channel')
    j = j + 1
    
img_corr_hsv = channel_corr(img_hsv)
plt.imshow(img_corr_hsv),plt.colorbar(),plt.xticks(range(3), ["Red", "Green", "Blue"]),plt.yticks(range(3), ["Red", "Green", "Blue"])
    
#Part 3
hue_channel = img_hsv[:,:,0]
saturation_channel = img_hsv[:,:,1]
value_channel = img_hsv[:,:,2]




    
