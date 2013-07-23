Access physical constants:
>>> from astropy import units as u
>>> from astropy import constants as c
>>> print c.G
  Name   = Gravitational constant
  Value  = 6.67384e-11
  Error  = 8e-15
  Units  = m3 / (kg s2)
  Reference = CODATA 2010

Combine quantities and constants:
>>> F = (c.G * (3 * c.M_sun) * (2 * u.kg) /
...      (1.5 * u.au) ** 2)
>>> F.to(u.N)
<Quantity 0.0158179542881 N>
