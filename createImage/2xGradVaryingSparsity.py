from photutils import datasets
from photutils.datasets import make_gaussian_sources
import matplotlib.pyplot as plt
import numpy as np
from astropy.table import Table
import matplotlib.image as mpimg
from matplotlib import rcParams
rcParams['font.size'] = 13

sigma_psf = 0.5
sources = Table()
sources['x_mean'] = [5, 15]
sources['y_mean'] = 2*[10]
sources['x_stddev'] = 4*sigma_psf*np.ones(2)
sources['y_stddev'] = sources['x_stddev']
sources['theta'] = 2*[0]
sources['id'] = [1]
sources['flux'] = [100, 100]

for i in range(1,11):
    length = 15+5*i
    tshape = (15+5*i, 15+5*i)
    sources['x_mean'] = [length/2-5, length/2+5]
    sources['y_mean'] = 2*[length/2]
    image = (make_gaussian_sources(tshape, sources) ) 
    #plt.imshow(image, cmap='Greys_r', aspect=1, interpolation='nearest', origin='lower')
    #plt.title('Simulated data')
    #plt.colorbar(orientation='horizontal', fraction=0.046, pad=0.04)
    #plt.axis('off')
    filename = "2xOutVaryingSparsity/out" + str(i) + ".png"
    mpimg.imsave(filename, image, cmap='Greys_r')

    #plt.show()