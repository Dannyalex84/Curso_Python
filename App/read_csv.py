import csv
# 1er metodo
def read_csv(path): # funcion abrir archivo
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        
         #nombre de las columnas se encuentra en la primera fila
        header = next(reader)
        # print(header)
        data = []
        for row in reader:
            iterable = zip(header, row) # une los valores de la listas en tuplas
            country_dict = {key: value for key, value in iterable} # mas largo el metodo
            data.append(country_dict)
        return data
# correr archivo como script desde la terminal
if __name__ == '__main__':
    data = read_csv('./data.csv')
    print(data)
    
# 2do metodo
# def read_csv(path): # funcion abrir archivo
#     with open(path, 'r') as csv_file:
#         reader = csv.reader(csv_file, delimiter=',')
        
#          #nombre de las columnas se encuentra en la primera fila
#         header = next(reader)
#         # print(header)
#         data = []
#         for row in reader:
#             population = {header[i]:row[i] for i in range(len(row))}
#             countries = dict(population) # Mas corto metodo
#             data.append(countries)
#         return data
# # correr archivo como script desde la terminal
# if __name__ == '__main__':
#     data = read_csv('./data.csv')
#     print(data)