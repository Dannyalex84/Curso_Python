lives = 3
print(type(lives))

age = 12
budget = 100

temperatura = 12.12
print(type(temperatura))

lives = 2
print(lives)
lives = 1
print(lives)

lives = 12 + 15
print(lives)

lives = lives - 1
print(lives)

lives -= 1
print(lives)

lives -= 5
print(lives)

lives += 5
print(lives)

number = 450000000000000000.1
print(number)

number_b = 0.0000000000000001
print(number_b)

# importa el modulo de statistics de python , el cual  permite realizar operaciones como suma,promedio,media etc. 
from statistics import mean
# capturar los valores correspondiente a cada mes
budgetEnero = int(input('ingrese el presupuesto de enero '))
budgetFebrero = int(input('ingrese el presupuesto de febrero '))
budgetMarzo = int(input('ingrese el presupuesto de marzo '))
# hallar el promedio, dentro de '[]' se puede agregar los valores de los meses separados por comas
mean = mean([budgetEnero, budgetFebrero, budgetMarzo])
# imprime el promedio
print(f'el promedio de los meses es {mean}')

# Forma larga

budget_january = input('¿Cual es tu presupuesto de enero? ') 
budget_february = input('¿Cual es tu presupuesto de febrero? ')
budget_march = input('¿Cual es tu presupuesto de marzo? ')

budget_january = int(budget_january)
budget_february = int(budget_february)
budget_march = int(budget_march)

budget_total = budget_january + budget_february + budget_march
print('La suma de los presupuestos es: ', budget_total)

budget_total = int(budget_total)

avg_budget = budget_total / 3
print('El promedio es: ', avg_budget)