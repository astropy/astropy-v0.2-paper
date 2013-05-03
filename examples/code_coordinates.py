Parse coordinate string
>>> import astropy.coordinates as coord
>>> c = coord.ICRSCoordinates('00h42m44.3s +41d16m9s')

Access the RA/Dec values
>>> c.ra
<RA 10.68458 deg>
>>> c.dec
<Dec 41.26917 deg>
>>> c.ra.degrees
10.684583333333332
>>> c.ra.hms
(0.0, 42, 44.299999999999784)

Convert to Galactic coordinates
>>> g = c.transform_to(coord.GalacticCoordinates)
>>> g.l
<Angle 121.17431 deg>
>>> g.b
<Angle -21.57280 deg>

Set the distance and view the cartesian coordinates
>>> from astropy import units as u
>>> c.distance = coord.Distance(770., u.kpc)
>>> c.x
568.7128882165681
>>> c.y
107.3009359688103
>>> c.z
507.8899092486349

Query the SIMBAD database
>>> m = coord.ICRSCoordinates.from_name("M42")
>>> m
<ICRSCoordinates RA=83.82208 deg, Dec=-5.39111 deg>