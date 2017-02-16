import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import cv2
import compressiveSense as CS

averageFluxes = []
sparsity = [.515,0.3408,0.2366,0.17387755,0.133125,0.10518,0.0852,0.070413,0.059166,0.050414]
error = [
    [2633.61588268,
    2954.75773065,
    3148.69586823,
    3275.54760163,
    3351.74796633],
                 
    [1574.88150114,
    1877.8363961 ,
    2079.75561171,
    2243.17940678,
    2331.89195028],
                 
    [880.900063729,
    1252.52503762,
    1508.52114952,
    1628.16331627,
    1734.01918336],
                 
    [315.442981207,
    745.009331421,
    975.82138391 ,
    1116.84703419,
    1234.10306891],
                 
    [23.7214673432,
    166.309882922,
    493.634818267,
    638.804729676,
    741.741584965],
                 
    [7.25747365698,
    48.3446818503,
    214.971157583,
    422.672130402,
    548.677476289],
                 
    [0.552265501288,
    39.5348149019,
    276.128337387,
    408.248227767,
    526.359195861],
    
    [2.19864564533e-06,
    1.82723302087,
    28.0736443773,
    130.318592319,
    277.560349924],
    
    [6.24801069671e-07,
    0.606152769071,
    6.08077170611,
    36.702018457,
    134.731646855],
    
    [1.49680642306e-06,
    1.61034876801e-06,
    0.831263681674,
    6.22454979456,
    29.110996399]
    
]    
    
def pltErrorVRatio():
    x_axis = [4,5,6,7,8]
    for i in range(10):
        plt.plot(x_axis, error[i], '-o')
    plt.xlabel('Compression Ratio')
    plt.ylabel('Average Error')
    plt.title('CS Error on a 1600 pixel image for varying sparsities')
    plt.axis([3, 9, 0, 3500])
    plt.legend(sparsity[0:10], loc='upper left')
    
    plt.show()
    
def pltErrorVSparsity():
    x_axis = sparsity
    for i in range(5):
        errorVals = [error[x][i] for x in range(10)]
        plt.plot(x_axis, errorVals, '-o')
    plt.xlabel('Sparsity')
    plt.ylabel('Average Error')
    plt.title('CS Error on a 1600 pixel image for varying compression ratios')
    #plt.axis([3, 9, 0, 3500])
    plt.legend([str(x+4)+"x compression ratio" for x in range(5)], loc='upper left')
    
    plt.show()   

pltErrorVRatio()    
