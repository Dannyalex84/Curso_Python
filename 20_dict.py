# Estructura original de los diccionarios

person = {
    'name': 'Danny',
    'last_name': 'Belandria',
    'langs': ['python', 'java', 'kotlin'],
    'age': 39
}

print(person)

# Se agrega contenido a la estructura original de los diccionarios

person['name'] = 'Juan'
person['age'] -= 20 # Resta esta cantidad person['age'] = person['age'] - 20
person['langs'].append('rust') # Agrega un elemento a la lista de los lenguajes de programacion
print(person)

del person['last_name']

print(person)
person.pop('age')

print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())
