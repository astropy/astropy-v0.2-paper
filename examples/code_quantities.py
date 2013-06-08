Define a quantity from scalars and units:
>>> from astropy import units as u
>>> 15.1 * u.m / u.s
<Quantity 15.1 m / s>

Convert a distance:
>>> (1.15e13 * u.km).to(u.pc)
<Quantity 0.372689618289 pc>

Make use of the unit equivalencies:
>>> e = 130. * u.eV
>>> e.to(u.Angstrom, equivalencies=u.spectral())
<Quantity 95.37245609234003 Angstrom>

Combine quantities:
>>> x = 1.4e11 * u.km / (0.7 * u.Myr)
>>> x
<Quantity 2e+11 km / Myr>

Convert to SI units:
>>> x.si
<Quantity 6.33761756281 m / s>

Convert to CGS units:
>>> x.cgs
<Quantity 633.761756281 cm / s>
