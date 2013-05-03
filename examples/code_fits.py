Read in a FITS file from disk
>>> from astropy.io import fits
>>> hdus = fits.open('sample.fits')

Access the header of the first HDU:
>>> hdus[0].header
SIMPLE  =                    T
BITPIX  =                  -32
NAXIS   =                    3
NAXIS1   =                 200
NAXIS2   =                 200
NAXIS2   =                  10
EXTEND  =                    T
...

Access the shape of the data in the first HDU:
>>> hdus[0].data.shape
(10, 200, 200)

Update/add header keywords
>>> hdus[0].header['TELESCOP'] = 'Python'
>>> hdus[0].header['INSTRUME'] = 'Computer'

Multiply data by 1.2
>>> hdus[0].data *= 1.2

Write out to disk
>>> hdus.writeto('new_file.fits')
