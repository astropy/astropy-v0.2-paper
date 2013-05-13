Create a custom cosmology object
>>> from astropy.cosmology import FlatLambdaCDM
>>> cosmo = FlatLambdaCDM(H0=70, Om0=0.3)
>>> cosmo
FlatLambdaCDM(H0=70, Om0=0.3, Ode0=0.7)

Compute the comoving volume to z=6.5 in cubic Mpc using
this cosmology
>>> cosmo.comoving_volume(6.5)
1074707289417.6837

Compute the age of the universe in Gyr using the
pre-defined WMAP 5-year and WMAP 9-year cosmologies
>>> from astropy.cosmology import WMAP5, WMAP9
>>> WMAP5.age(0)
13.723782349795023
>>> WMAP9.age(0)
13.768899510689097

Create a cosmology with a varying `w'
>>> from astropy.cosmology import Flatw0waCDM
>>> cosmo = Flatw0waCDM(H0=70, Om0=0.3, w0=-1, wa=0.2)

Find the separation in proper kpc at z=4 corresponding to
10 arcsec in this cosmology compared to a WMAP9 cosmology
>>> cosmo.kpc_proper_per_arcmin(4) * 10 / 60.
68.87214405278925
>>> WMAP9.kpc_proper_per_arcmin(4) * 10 / 60.
71.21374615575363
