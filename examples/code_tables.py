Create an empty table and add columns
>>> from astropy.table import Table, Column
>>> t = Table()
>>> t.add_column(Column(data=['a', 'b', 'c'],
...                     name='source'))
>>> t.add_column(Column(data=[1.2, 3.3, 5.3],
...                     name='flux'))
>>> print t
source flux
------ ----
     a  1.2
     b  3.3
     c  5.3
     
Read a table from a file
>>> t1 = Table.read('catalog.vot')
>>> t1 = Table.read('catalog.tbl', format='ipac')
>>> t1 = Table.read('catalog.cds', format='cds')

Extract subsets of tables
>>> t2 = t1[t1['flux'] > 5.0]

Manipulate columns
>>> t2.remove_column('J_mag')
>>> t2.rename_column('Source', 'sources')

Write a table to a file
>>> t2.write('new_catalog.hdf5')
>>> t2.write('new_catalog.rdb')
>>> t2.write('new_catalog.tex')

