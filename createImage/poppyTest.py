import matplotlib.pyplot as plt
import poppy
import numpy as np
import matplotlib.image as mpimg

def convolve(im1, im2, size):
    convolvedArray = []
    for i in range(size):
        convolvedArray.append(np.convolve(im1[i*size:(i+1)*size], im2[i*size:(i+1)*size], 'same'))
    return convolvedArray

osys = poppy.OpticalSystem()
osys.add_pupil( poppy.GaussianAperture(fwhm = 0.5))    # pupil radius in meter  
osys.add_detector(pixelscale= 1, fov_arcsec= 6.0)  # image plane coordinates in arc seconds
psf = osys.calc_psf(2e-6) 
psfdata = psf[0].data

image1 = np.zeros((12,12))
image2 = np.zeros((12,12))

#FILL UP CENTER OF BASE IMAGE WITH WHITE
base = 1
image1[5][5]=base
image1[5][6]=base
image1[6][5]=base
image1[6][6]=base

image2[5][5]=base
image2[5][6]=base
image2[6][5]=base
image2[6][6]=base

#ADD IN PSF
image1Flat = image1.ravel()
image2Flat = image2.ravel()
psfFlat = psfdata.ravel()
print(len(psfFlat))

image1PSFFlat = convolve(image1Flat,psfFlat,12)
image2PSFFlat = convolve(image2Flat,psfFlat+psfFlat,12)

image1PSF = np.reshape(image1PSFFlat, (12,12))
image2PSF = np.reshape(image2PSFFlat, (12,12))

plt.figure()
plt.imshow(image1, origin='lower', cmap='gray',clim=(0.0, 1.452))
mpimg.imsave('psf.png', image1PSF, cmap='gray',vmin=0.0, vmax=1.0)

mpimg.imsave('poppyPoint1.png', image1PSF, cmap='gray',vmin=0.0, vmax=1.0)
mpimg.imsave('poppyPoint2.png', image2PSF, cmap='gray',vmin=0.0, vmax=1.0)

print(psfdata)

plt.axis('off')
plt.show()