
# len
set_countries = {'col', 'mex', 'bol'}
size = len(set_countries)
print(size)

print('col' in set_countries)
print('per' in set_countries)

# add
set_countries.add('per')
print(set_countries)
set_countries.add('per')
print(set_countries)

# update
set_countries.update({'arg', 'ecua', 'per'})
print(set_countries)

# remove
set_countries.remove('col')
print(set_countries)

set_countries.remove('arg')
set_countries.discard('ar')
print(set_countries)
set_countries.clear()
print(set_countries)
print(len(set_countries))

