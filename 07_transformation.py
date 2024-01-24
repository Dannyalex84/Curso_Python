name = 'Danny'
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

print('Danny' + ' Belandria')
print(10 + 20)
print('Danny' + '12')

age = 12
print('Mi edad es: ' + str(age))
print(f'Mi edad es: {age}')

age = input('Escribe tu edad => ')
print(type(age))
age = int(age)
age += 10
print(f'Tu edad en 10 años sera {age}')

# Ejercicio practico

name = 'Juana'
print(name)
age = '10'
print(age)

total = int(age)
total +=10
template = f"Hola mi nombre es {name}, tengo {age} y en 10 años tendre {total} años"
print(template)