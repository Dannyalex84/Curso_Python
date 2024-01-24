set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# Union
set_c = set_a.union(set_b)
print(set_c)
print((set_a | set_b))

# Interseccion
set_d = set_a.intersection(set_b)
print(set_d)
print((set_a & set_b))

# Diferencia
set_e = set_a.difference(set_b)
print(set_e)
print((set_a - set_b))

# Diferencia simetrica
set_e = set_a.symmetric_difference(set_b)
print(set_e)
print((set_a ^ set_b))


