import time

def fibo_gen(max):
#     n1 = 0
#     n2 = 1
#     counter = 0
#     while True:
        
#         if counter == 0:
#             counter += 1
#             yield n1
            
#         elif counter == 1:
#             counter += 1
#             yield n2
            
#         else:
#             aux = n1 + n2
#             n1, n2 = n2, aux
#             counter += 1
#             if aux > max:
#                 print("Finalizar")
#                 raise StopIteration
#             yield aux
            
# # def run():
# if __name__ == '__main__':
#     max = int(input("Numero maximo: "))
#     fibonacci = fibo_gen(max)
#     for element in fibonacci:
#         print(element)
#         time.sleep(0.05)
        

    # run()
    
    
    n1, n2, count = 0, 1, 1
    while True:
        if count <= max:
            count += 1
            yield n1 
            n1, n2 = n2, n1 + n2
        else:
            if count > max:
                print("Listo, Terminamos...")
            return

if __name__ == "__main__":
    max = int(input("Sucesiones maximas: "))
    fibonacci = fibo_gen(max)
    for element in fibonacci:
        print(element)
        time.sleep(0.05)