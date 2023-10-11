def my_set():
    my_set1 = {5, 9, 10, 11, 12, 13, 14, 15}
    my_set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    
    # Union
    my_set3 = my_set1 | my_set2
    print(my_set3)

    # Interseccion
    
    my_set4 = my_set1 & my_set2
    print(my_set4)
    
    # Diferencia Simple
    
    my_set5 = my_set1 - my_set2
    print(my_set5)
    
    my_set6 = my_set2 - my_set1
    print(my_set6)
    
    # Diferencia Simentrica
    
    my_set7 = my_set1 ^ my_set2
    print(my_set7)
    

if __name__ == "__main__":
    my_set()
    