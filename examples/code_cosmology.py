Create a custom cosmology object:
>>> from astropy.cosmology import FlatLambdaCDM
>>> cosmo = FlatLambdaCDM(H0=70, Om0=0.3)
>>> cosmo
FlatLambdaCDM(H0=70, Om0=0.3, Ode0=0.7)

Compute comoving volume at z=6.5
>>> cosmo.comoving_volume(6.5)
1074707289417.6837
