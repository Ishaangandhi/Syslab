import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import cv2
import compressiveSense as CS
import calculateSparsity as calcSparsity
from multiprocessing import Pool, Value

'''
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
'''
def calculateError(image1, image2):
    totalError = 0.0
    pixelSpace1 = image1.flatten()
    pixelSpace2 = image2.flatten()
    numPixels = len(pixelSpace1)
    for i in range(numPixels):
        totalError+=(pixelSpace1[i]-pixelSpace2[i])**2
    return (totalError/numPixels)
'''''
def calculateAverageFlux(inputImage):
    totalFlux = 0.0
    numPixels = 0
    for pixelIntensity in inputImage.flatten():
        totalFlux+=pixelIntensity
        numPixels+=1.0
    return (totalFlux/numPixels)

compressionMatrixSizes = [i*20+200 for i in range(10)]
errorForSize = []
'''
    
NUMTRIALS = 100

def compressAndRecoverNP(input):
    (curImage, compressionSize) = input
    return np.array(CS.runCS(curImage,False,compressionSize))

for i in range(1,11):
    totalErrorSize4 = 0
    totalErrorSize5 = 0
    totalErrorSize6 = 0
    totalErrorSize7 = 0
    totalErrorSize8 = 0
    
    print("*************")
    string = 'createImage/2xOutVaryingSparsity/out' + str(i) + '.png'
    print(string)
    curImage = cv2.imread(string,0) #READ IN WITH CV2
    curSparsity = calcSparsity.calculateSparsity(string)
    print("Sparsity: ", curSparsity)
    width,height = curImage.shape[:2]
    compressionSize4 = int((height**2)/4)
    compressionSize5 = int((height**2)/5)
    compressionSize6 = int((height**2)/6)
    compressionSize7 = int((height**2)/7)
    compressionSize8 = int((height**2)/8)
    for trials in range(NUMTRIALS):
        '''result4 = np.array(CS.runCS(curImage,False,compressionSize4))
        result5 = np.array(CS.runCS(curImage,False,compressionSize5))
        result6 = np.array(CS.runCS(curImage,False,compressionSize6))
        result7 = np.array(CS.runCS(curImage,False,compressionSize7))
        result8 = np.array(CS.runCS(curImage,False,compressionSize8))'''
        p = Pool(5)
        imageArg = [(curImage, compressionSize4),
            (curImage, compressionSize5),
            (curImage, compressionSize6),
            (curImage, compressionSize7),
            (curImage, compressionSize8)]
        results = p.map(compressAndRecoverNP, imageArg)
        p.close()
        p.join()
        curError4 = calculateError(curImage, results[0])
        curError5 = calculateError(curImage, results[1])
        curError6 = calculateError(curImage, results[2])
        curError7 = calculateError(curImage, results[3])
        curError8 = calculateError(curImage, results[4])
        totalErrorSize4+=curError4
        totalErrorSize5+=curError5
        totalErrorSize6+=curError6
        totalErrorSize7+=curError7
        totalErrorSize8+=curError8
        
    print("4x Compression error: ", str(totalErrorSize4/NUMTRIALS))
    print("5x Compression error: ", str(totalErrorSize5/NUMTRIALS))
    print("6x Compression error: ", str(totalErrorSize6/NUMTRIALS))
    print("7x Compression error: ", str(totalErrorSize7/NUMTRIALS))
    print("8x Compression error: ", str(totalErrorSize8/NUMTRIALS))
