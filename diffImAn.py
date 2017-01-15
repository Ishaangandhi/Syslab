import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pylab as py
from cvxpy import *
from dia3 import dia
from dia3 import dialin

def runDIA(referenceImage, observedImage):
    imageRef = cv2.imread(referenceImage,0) #READ IN WITH CV2
    (m,n) = imageRef.shape

    image2 = cv2.imread(observedImage,0) #READ IN WITH CV2
    imageRef = imageRef.astype(np.int16)
    image2 = image2.astype(np.int16)
    
    '''
    imageRef = py.zeros((10,10))
    image2 = py.zeros((10,10))
    imageRef[3,3] = 1; imageRef[3,6] = 1;  refimageRef = 1
    image2[2,3] = 1; image2[3,2:5] = 1;  image2[4,3] = 1
    image2[2,6] = 1; image2[3,5:8] = 1;  image2[4,6] = 1
    image2[5,3] = 1; image2[6,2:5] = 1;  image2[7,3] = 1
    
    m = 10
    n = 10
'''
    imgSubtraction = image2-imageRef
    print(imageRef[1])
    print(image2[1])
    print(imgSubtraction[1])
    
    kb = np.ones((10,10)) # DEFINE THE KERNEL BASIS
    #print(kb)
    #kb=[[0,0,0],[0,1,0],[0,0,0]]
    # Compute Difference Image Analysis:
    #m, kern, bkg, chisq = dialin(imageRef, image2, kb,noback=True)
    m, kern, bkg, chisq = dia(imageRef, image2, kb,noback=True)

    # Display results:
    plt.figure(figsize=(10,8))
    
    plt.subplot(231)
    plt.imshow(imageRef, cmap='Greys_r')
    plt.title('Reference image')
    plt.colorbar(orientation='horizontal', fraction=0.046, pad=0.10)
    
    plt.subplot(232)
    plt.imshow(image2, cmap='Greys_r')
    plt.title('Observed image')
    plt.colorbar(orientation='horizontal', fraction=0.046, pad=0.10)
    
    plt.subplot(233)
    plt.imshow(imgSubtraction, cmap='Greys_r')
    plt.title('Pure subtraction')
    plt.colorbar(orientation='horizontal', fraction=0.046, pad=0.10)
    
    plt.subplot(234)
    plt.imshow(kern, cmap='Greys_r')
    plt.title('Optimal kernel')
    plt.colorbar(orientation='horizontal', fraction=0.046, pad=0.10)
    
    plt.subplot(235)
    plt.imshow(m, cmap='Greys_r')
    plt.title('Convolved Reference')
    plt.colorbar(orientation='horizontal', fraction=0.046, pad=0.10)
    
    plt.subplot(236)
    plt.imshow(image2 - m, cmap='Greys_r')
    plt.title('Residuals')
    plt.colorbar(orientation='horizontal', fraction=0.046, pad=0.10)
    
    plt.show()
    
if __name__=="__main__":
    reference = 'createImage/doubleOut/out14.png'
    observed = 'createImage/doubleOut/out15.png'
    runDIA(reference, observed)