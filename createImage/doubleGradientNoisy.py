from photutils import datasets
from photutils.datasets import make_gaussian_sources
import matplotlib.pyplot as plt
import numpy as np
from astropy.table import Table
import matplotlib.image as mpimg
from matplotlib import rcParams
from photutils.datasets import make_noise_image

rcParams['font.size'] = 13

sigma_psf = 0.5
sources = Table()
sources['x_mean'] = [10, 30]
sources['y_mean'] = 2*[20]
sources['x_stddev'] = 3*sigma_psf*np.ones(2)
sources['y_stddev'] = sources['x_stddev']
sources['theta'] = 2*[0]
sources['id'] = [1]
tshape = (40, 40)

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
for (count,i) in enumerate(B):
    sources['flux'] = [900,7*i]
    image = make_gaussian_sources(tshape, sources) + make_noise_image(tshape, type='gaussian', mean=1.,
                                   stddev=0.5)
    plt.imshow(image, cmap='Greys_r', aspect=1, interpolation='nearest',
    origin='lower')
    plt.axis('off')
    filename = "doubleOutNoisy/out" + str(count) + ".png"
    
   # filename = "doubleOutNoisyWide/out" + str(count) + ".png"
    mpimg.imsave(filename, image, cmap='Greys_r')

    plt.show()