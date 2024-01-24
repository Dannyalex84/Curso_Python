price = 100 # Global scope
result = 200

def increment():
    price = 200
    result = price + 10 # Local scope
    print(result)
    return result

print(price)
price_2 = increment()
print(price_2)
print(result)