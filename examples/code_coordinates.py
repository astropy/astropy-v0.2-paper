Parse coordinate string
>>> import astropy.coordinates as coords
>>> c = coords.ICRSCoordinates('00h42m44.3s +41d16m9s')

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
>>> c.galactic.l
<Angle 121.17431 deg>
>>> c.galactic.b
<Angle -21.57280 deg>

Create a separate object in Galactic coordinates
>>> g = c.transform_to(coords.GalacticCoordinates)
>>> g.l.format('degree', sep=':', precision=3)
'121:10:27.499'

Set the distance and view the cartesian coordinates
>>> from astropy import units as u
>>> c.distance = coords.Distance(770., u.kpc)
>>> c.x
568.7128882165681
>>> c.y
107.3009359688103
>>> c.z
507.8899092486349

Query SIMBAD to get coordinates from object names
>>> m = coords.ICRSCoordinates.from_name("M32")
>>> m
<ICRSCoordinates RA=10.67446 deg, Dec=40.86589 deg>

Two coordinates can be used to get distances
>>> m.distance = coords.Distance(765., u.kpc)
>>> m.separation_3d(c)
<Distance 7.36155 kpc>
