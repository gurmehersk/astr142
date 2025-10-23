import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from datetime import datetime


# Image size
width, height = 512, 512

# Create a meshgrid of x and y values
x = np.linspace(0, 4*np.pi, width)  
y = np.linspace(0, 4*np.pi, height) 
X, Y = np.meshgrid(x, y)

# Create sinusoidal wave interference pattern
Z = np.sin(X) + np.sin(Y)

# Normalize
Z_normalized = ((Z - Z.min()) / (Z.max() - Z.min()))

# Display the image
plt.imshow(Z_normalized, cmap='gray', origin='upper')
plt.colorbar()
plt.title('2D Interference Pattern')
plt.show()

prim_hdu = fits.PrimaryHDU(Z_normalized)
prim_hdu.header['OBJECT'] = 'interference pattern'
prim_hdu.header['AUTHOR'] = 'Gurmeher Kathuria'
prim_hdu.header['DATE'] = datetime.now().strftime('%Y-%m-%d')

x_g = np.linspace(0, width-1, width)
y_g = np.linspace(0, height-1, height)
X, Y = np.meshgrid(x_g, y_g)
x0, y0 = width/2, height/2
sig = 50

# gaussian function formula
gaussian_function = np.exp(-((X-x0)**2 + (Y-y0)**2) / (2*sig**2))

g_hdu = fits.ImageHDU(gaussian_function)
g_hdu.header['EXTNAME'] = 'my_gaussian'

hdu_list = fits.HDUList([prim_hdu, g_hdu])
hdu_list.writeto('int_op.fits')



