Parse a date/time in ISO format and on the UTC scale
>>> from astropy.time import Time
>>> t = Time('2010-06-01 00:00:00',
             format='iso', scale='utc')
>>> t
<Time object: scale='utc' format='iso'
              vals=2010-06-01 00:00:00.000>

Access the time in Julian Date format
>>> t.jd
2455348.5

Access the time in year:day:time format
>>> t.yday
'2010:152:00:00:00.000'

Convert time to the TT scale
>>> t.tt
<Time object: scale='tt' format='iso'
              vals=2010-06-01 00:01:06.184>

Find the julian date in the TT scale
>>> t.tt.jd
2455348.5007660184
