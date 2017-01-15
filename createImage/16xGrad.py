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
sources['x_mean'] = [10+x*20 for x in range(4)]*4
sources['y_mean'] = [10+x*20 for x in range(4) for y in range(4)]
print(sources['y_mean'])
sources['x_stddev'] = 3*sigma_psf*np.ones(16) #change 3 to 5 for wide PSF
sources['y_stddev'] = sources['x_stddev']
sources['theta'] = 16*[0]
sources['id'] = [1]
tshape = (80, 80)

length = 30
te=30
t0=15
u0=.01
B=[0]*length

for t in range(0,length):
    print (t)
    tf = (t- t0)/te;
    u = (u0**2 + tf**2)**(1/2);
    B[t] = (u**2 + 2)/ (u*(u**2 +4)**(1/2)); 
print(B)
sources['flux']=[900]*16
for (count,i) in enumerate(B):
    sources['flux'][15] = 7*i
    image = (make_gaussian_sources(tshape, sources) ) 
    plt.imshow(image, cmap='Greys_r', aspect=1, interpolation='nearest',
    origin='lower')
    #plt.title('Simulated data')
    #plt.colorbar(orientation='horizontal', fraction=0.046, pad=0.04)
    plt.axis('off')
    filename = "16xOut/out" + str(count) + ".png"
    mpimg.imsave(filename, image, cmap='Greys_r')

   # plt.show()