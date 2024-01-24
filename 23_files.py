file = open('./text.txt')
#print(file.read()) 'Todo el archivo'
# print(file.readline()) #'Leer linea a linea'
# print(file.readline()) #'Leer linea a linea'
# print(file.readline()) #'Leer linea a linea'
# print(file.readline()) #'Leer linea a linea'

for line in file:
    print(line) #'Leer linea a linea'

file.close()

with open('./text.txt') as file:
    for line in file:
        print(line)
        