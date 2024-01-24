try:
    print(0/0)
    assert 1 != 1, 'No es igual'
    age = 10
    if age < 18:
        raise Exception('No eres mayor de edad')
except ZeroDivisionError as error:
    print(error)
except ZeroDivisionError as error:
    print(error)
except Exception as error:
    print(error)
    
print('Hola')

def my_divide(a, b):
   # Escribe tu solución 👇
   try:
      result = a / b
   except ZeroDivisionError as error:
      result = 'No se puede dividir por 0'
   return result
    
response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response) # No se puede dividir por 0
