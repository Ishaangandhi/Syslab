import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import cv2
import compressiveSense as CS
import calculateSparsity as calcSparsity
from multiprocessing import Pool, Value


def calculateError(image1, image2):
    totalError = 0.0
    pixelSpace1 = image1.flatten()
    pixelSpace2 = image2.flatten()
    numPixels = len(pixelSpace1)
    for i in range(numPixels):
        totalError+=(pixelSpace1[i]-pixelSpace2[i])**2
    return (totalError/numPixels)
    
NUMTRIALS = 5

def compressAndRecoverNP(input):
    (curImage, compressionSize) = input
    return np.array(CS.runCS(curImage,False,compressionSize))

for i in range(1,11):
    totalErrorSize4 = 0
    totalErrorSize8 = 0
    
    print("*************")
    string = 'createImage/2xNoisyOutVaryingSparsity/out' + str(i) + '.png'
    print(string)
    curImage = cv2.imread(string,0) #READ IN WITH CV2
    curSparsity = calcSparsity.calculateSparsity(string)
    print("Sparsity: ", curSparsity)
    width,height = curImage.shape[:2]
    compressionSize4 = int((height**2)/4)
    compressionSize8 = int((height**2)/8)
    for trials in range(NUMTRIALS):
        p = Pool(2)
        imageArg = [(curImage, compressionSize4),
            (curImage, compressionSize8)]
        results = p.map(compressAndRecoverNP, imageArg)
        p.close()
        p.join()
        curError4 = calculateError(curImage, results[0])
        curError8 = calculateError(curImage, results[1])
        totalErrorSize4+=curError4
        totalErrorSize8+=curError8
        
    print("4x Compression error: ", str(totalErrorSize4/NUMTRIALS))
    print("8x Compression error: ", str(totalErrorSize8/NUMTRIALS))
