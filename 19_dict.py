my_dict = {}
print(type(my_dict))

my_dict = {
    'avion': 'bla bla bla',
    'name': 'Danny',
    'last_name': 'Belandria',
    'age': 39 
}
print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['name'])
print(my_dict['last_name'])
print(my_dict.get('age'))
print(my_dict.get('unvalor'))
print('avion' in my_dict)
print('unvalor' in my_dict)