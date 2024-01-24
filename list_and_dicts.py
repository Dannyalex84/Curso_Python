def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Danny", "lastname": "Belandria"}
    
    super_list = [
        {"firstname": "Danny", "lastname": "Belandria"},
        {"firstname": "Karina", "lastname": "Giraldo"},
        {"firstname": "Carol", "lastname": "Ramirez"},
        {"firstname": "Anthuan", "lastname": "Morales"},
        {"firstname": "Diego", "lastname": "Belandria"},
        {"firstname": "Rubiela", "lastname": "Giraldo"},
    ]
    
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }
    
    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == '__main__':
    run()