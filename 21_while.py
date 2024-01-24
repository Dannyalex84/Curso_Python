if True:
    print("se ejecuto")
    

''' while True:
    print("se ejecuto")'''

counter = 0
# while counter <= 10:
#     print(counter)
#     counter = counter + 1
 
# while counter < 10:
#     counter += 1
#     print(counter)

# while counter < 20:
#     counter += 1
#     if counter == 15:
#         break
#     print(counter)

# while counter < 20:
#     counter += 1
#     print(counter)

while counter < 20:
    counter += 1
    if counter < 15: # Corta la ejecucion del bucle de 20 a 15
        continue
    print(counter)