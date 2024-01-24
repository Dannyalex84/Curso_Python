def increment(x):
    return x + 1

increment_2 = lambda x: x + 1

def high_ord_func(x, func):
    return x + func(x)

high_ord_func_2 = lambda x, func: x + func(x)

result = high_ord_func(2, increment)
# 2 + (2 + 1)
print(result)

result = high_ord_func_2(2, increment_2)
print(result)
result = high_ord_func_2(2, lambda x: x + 2)
print(result)
# change the function
result = high_ord_func_2(2, lambda x: x * 2)
print(result)