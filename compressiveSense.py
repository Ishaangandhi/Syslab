import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import cv2
from cvxpy import *
from dia3 import *

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
     
def runCS(image1, showPlot, numMeasurements):
    (m,n) = image1.shape
    image2 = np.reshape(image1,(1,m*n))
    #print(image1)

    #CHOOSE A MATRIX TO BE GAUSSIAN OR BERNOULLI
    A = np.random.binomial(1, 0.5, size = [numMeasurements,m*n]); 
    #numMeasurements (width of sensing matrix) ~= 400
    #A = 5*np.random.randn(400, m*n)

    #MULTIPLY MATRICES
    b = np.dot(A,image2.T);

    #SET UP OPTIMIZATIONS
    x = Variable(m*n)

    objective = Minimize(norm((A*x - b), 1))
    constraints = [ 0 <= x]

    #objective = Minimize(norm((x), 1))
    #constraints = [abs(A*x-b) < .0001, 0<=x]

    prob = Problem(objective, constraints)
    prob.solve(solver=SCS, max_iters=25000)

    recoveredImage = np.reshape(x.value,(m,n))

    #PLOT RESULTS
    if showPlot:
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))
        ax1.imshow(image1, origin='lower', interpolation='nearest', cmap='Greys_r')
        ax2.imshow(recoveredImage, origin='lower', interpolation='nearest', cmap='Greys_r')
        plt.show()
        
    return recoveredImage
    
if __name__ == "__main__":
    #image1 = rgb2gray(mpimg.imread("out.png")) #READ IN WITH MPL AND RGB2GRAY
    image1 = cv2.imread('createImage/doubleOut/out1.png',0) #READ IN WITH CV2
    runCS(image1)