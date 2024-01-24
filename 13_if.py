if True:
    print('deberia ejecutarse')
    
if False:
    print('no deberia ejecutarse')

# Primera forma de comparacion

'''pet = input('¿Cual es tu mascota favorita? ')

if pet == 'perro':
    print('genial tienes buen gusto')
    
if pet == 'gato':
    print('espero tengas suerte')
    
if pet == 'pez':
    print('eres lo maximo')'''
    
# Segunda forma de comparacion

pet = input('¿Cual es tu mascota favorita? ')

if pet == 'perro':
    print('genial tienes buen gusto')
elif pet == 'gato':
    print('espero tengas suerte')
elif pet == 'pez':
    print('eres lo maximo')
else:
    print('no tienes ninguna mascota')



'''stock = int(input('Digita el stock => '))

if stock >= 100 and stock <= 1000:
    print('stock es correcto')
else:
    print('el stock es incorrecto')'''
    
    
numero = int(input('Ingresa un numero: '))
if numero % 2 == 0:
    print('Es un numero par')
else:
    print('Es un numero impar')