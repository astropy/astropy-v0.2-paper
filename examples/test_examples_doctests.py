# Tests should be run with Python 2.7

import os
import numpy as np
import astropy
from astropy.io import fits
from astropy.table import Table

print "Testing Astropy v{0}".format(astropy.__version__)


CATALOG_IPAC = """| Source | flux  | J_mag  |
| char   | float | float  |
  a         1.      3.
  b         6.      5.
  c        10.      -1.
"""

open('catalog.tbl', 'w').write(CATALOG_IPAC)

CATALOG_CDS = """Title: Test table
Authors: Astropy
Table: Test
================================================================================
Byte-by-byte Description of file: data.txt
--------------------------------------------------------------------------------
   Bytes Format Units  Label   Explanations
--------------------------------------------------------------------------------
       1 A1     ---    Source  Source name
   4-  7 F4.1   ---    flux    Flux
  10- 13 F4.1   ---    J_mag   J magnitude
--------------------------------------------------------------------------------
a   1.0   3.0
b   6.0   5.0
c  10.0  -1.0
"""


def cleanup():

    files = ['catalog.cds', 'catalog.tbl', 'catalog.vot', 'new_catalog.hdf5',
             'new_catalog.rdb', 'new_catalog.tex', 'new_file.fits', 'sample.fits']

    for filename in files:
        if os.path.exists(filename):
            os.remove(filename)


def write_required_files():

    open('catalog.tbl', 'w').write(CATALOG_IPAC)

    open('catalog.cds', 'w').write(CATALOG_CDS)

    t = Table.read('catalog.tbl', format='ipac')
    t.write('catalog.vot', format='votable', overwrite=True)

    hdu0 = fits.PrimaryHDU(np.zeros((10, 200, 200), dtype=np.float32))
    hdu0.header.comments['SIMPLE'] = ""
    hdu0.header.comments['BITPIX'] = ""
    hdu0.header.comments['NAXIS'] = ""

    hdu1 = fits.ImageHDU(np.zeros((10, 200, 200), dtype=np.float32))
    hdulist = fits.HDUList([hdu0, hdu1])

    hdulist.writeto('sample.fits', clobber=True)


def preprocess(string):

    code = False
    lines = []

    for line in string.splitlines():

        # EXCEPTIONS - things where we know the output has been deliberately modified for the paper

        # FITS header is padded to 80 characters

        if line.startswith(('SIMPLE', 'BITPIX', 'NAXIS', 'EXTEND')):
            line = "%-80s" % line

        # Don't want to clutter examples with unicode u'' in output
        if line.startswith("'121"):
            line = 'u' + line

        if code:
            if line.strip() == "":
                code = False
        else:
            if line.startswith('>>>'):
                code = True

        if code:
            if line.startswith(' ') and '>' in line:
                lines[-1] += ' ' + line.strip()
            else:
                lines.append(line)

    return '\n'.join(lines)


def test_fig_1():
    pass

test_fig_1.__doc__ = preprocess(open('code_quantities.py', 'r').read())


def test_fig_2():
    pass

test_fig_2.__doc__ = preprocess(open('code_constants.py', 'r').read())


def test_fig_3():
    pass

test_fig_3.__doc__ = preprocess(open('code_time.py', 'r').read())


def test_fig_4():
    pass

test_fig_4.__doc__ = preprocess(open('code_coordinates.py', 'r').read())


def test_fig_5():
    pass

test_fig_5.__doc__ = preprocess(open('code_tables.py', 'r').read())


def test_fig_6():
    pass

test_fig_6.__doc__ = preprocess(open('code_fits.py', 'r').read())


def test_fig_7():
    pass

test_fig_7.__doc__ = preprocess(open('code_cosmology.py', 'r').read())

if __name__ == "__main__":
    import doctest
    cleanup()
    write_required_files()
    doctest.testmod()
    cleanup()
