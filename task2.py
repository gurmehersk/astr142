from astropy.io import fits
import numpy as np


input_filename = 'discussion08_example.fits'
output_filename = 'disc08_output.fits'

with fits.open(input_filename) as hdul:
    print("Original FITS file info:")
    hdul.info()
    
    # scaling the data by 10 [mag]
    hdul[0].data = hdul[0].data * 10
    hdul[0].header['SCALE'] = 10.0
    
    hdul.writeto(output_filename)

print(f"Created '{output_filename}'")
print("Data has been scaled by 10x")
