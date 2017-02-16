import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import cv2

string = 'ds9.png'
curImage = cv2.imread(string,0) #READ IN WITH CV2

for i in range(0,10):
    lowBound = 4*i
    highBound = 90 - 4*i
    image = curImage[lowBound:highBound,lowBound:highBound]
    filename = "2xTT" + str(i+1) + ".png"
    mpimg.imsave(filename, image, cmap='Greys_r')