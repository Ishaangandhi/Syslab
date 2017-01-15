from photutils import datasets
import matplotlib.pyplot as plt
import numpy as np
from photutils.datasets import make_noise_image
# make a table of Gaussian sources
from astropy.table import Table
table = Table()
table['amplitude'] = [50, 70, 150, 210]
table['flux'] = [1000, 1000, 1000, 1000]
table['x_mean'] = [160, 25, 150, 90]
table['y_mean'] = [70, 40, 25, 60]
table['x_stddev'] = [15.2, 5.1, 3., 8.1]
table['y_stddev'] = [2.6, 2.5, 3., 4.7]
table['theta'] = np.array([145., 20., 0., 60.]) * np.pi / 180.

# make an image of the sources without noise, with Gaussian
# noise, and with Poisson noise
from photutils.datasets import make_gaussian_sources
from photutils.datasets import make_noise_image
import matplotlib.image as mpimg

shape = (100, 200)
image1 = make_gaussian_sources(shape, table)
image2 = image1 + make_noise_image(shape, type='gaussian', mean=5.,
                                   stddev=5.)
image3 = image1 + make_noise_image(shape, type='poisson', mean=5.)

# plot the images
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))
ax1.imshow(image1, origin='lower', interpolation='nearest')
ax2.imshow(image2, origin='lower', interpolation='nearest')
ax3.imshow(image3, origin='lower', interpolation='nearest')

mpimg.imsave("out.png", image1)

plt.show()