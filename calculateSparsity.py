import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pylab as py

def calculateSparsity(referenceImage):
    imageRef = cv2.imread(referenceImage,0) #READ IN WITH CV2
    (m,n) = imageRef.shape
    flattenedImage = imageRef.flatten()
    brightestPixel = 0
    for i in range(m*n):
        if flattenedImage[i] > brightestPixel:
            brightestPixel = flattenedImage[i]
    
    sparseCount = 0        
    for i in range(m*n):
        if flattenedImage[i] > brightestPixel*.01:
            sparseCount+=1
            
    return sparseCount*1.0/(m*n)
    
if __name__=="__main__":
    #reference = 'createImage/doubleOut/out15.png'
    reference = 'createImage/2xTTSparsity/2xTT10.png'
    returned = calculateSparsity(reference)
    print("sparsity: ", returned)