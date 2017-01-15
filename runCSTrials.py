import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import cv2
import compressiveSense as CS

averageFluxes = []

def pltFlux():
    plt.plot(averageFluxes, 'ro')
    plt.xlabel('Image Number')
    plt.ylabel('Average Flux')
    plt.title('Magnification Curve')
    #plt.axis([0, 6, 0, 20])
    plt.show()
    
def pltError():
    plt.plot(compressionMatrixSizes, errorForSize,  'ro')
    plt.xlabel('Measurements')
    plt.ylabel('Average Error')
    plt.title('CS Error on a 1600 pixel image')
    #plt.axis([0, 6, 0, 20])
    plt.show()    
    
def calculateError(image1, image2):
    totalError = 0.0
    pixelSpace1 = image1.flatten()
    pixelSpace2 = image2.flatten()
    numPixels = len(pixelSpace1)
    for i in range(numPixels):
        totalError+=(pixelSpace1[i]-pixelSpace2[i])**2
    return (totalError/numPixels)

def calculateAverageFlux(inputImage):
    totalFlux = 0.0
    numPixels = 0
    for pixelIntensity in inputImage.flatten():
        totalFlux+=pixelIntensity
        numPixels+=1.0
    return (totalFlux/numPixels)

compressionMatrixSizes = [i*20+200 for i in range(10)]
errorForSize = []

for size in compressionMatrixSizes:
    totalError = 0
    for i in range(0,30):
        string = 'createImage/doubleOut/out' + str(i) + '.png'
        curImage = cv2.imread(string,0) #READ IN WITH CV2
        result = CS.runCS(curImage,False,size)
        npResult = np.array(result) #trasnform recovered image to numpy array to calculate AF
        curError = calculateError(curImage, npResult)
        totalError+=curError
        curAF = calculateAverageFlux(npResult)
        averageFluxes.append(curAF)
    errorForSize.append(totalError/30)
    print(totalError/30)
     
pltError()    
