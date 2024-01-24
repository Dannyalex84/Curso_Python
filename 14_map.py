numbers = [1, 2, 3, 4, 5]
numbers_2 = []
for i in numbers:
    numbers_2.append(i * 2)

numbers_3 = list(map(lambda i: i * 2, numbers))

print(numbers)
print(numbers_2)
print(numbers_3)

numbers_0 = [1, 2, 3, 4]
numbers_1 = [5, 6, 7]

print(numbers_0)
print(numbers_1)
result = list(map(lambda x, y: x + y, numbers_0, numbers_1))  # [6, 8, 10, 12]

print(result)