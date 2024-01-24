def find_volume(length=1, width=1, height=1, depth=1):
    return length * width * height * depth

result = find_volume()

print(result)


def find_volume_1(length, width, height, depth):
    return length * width * height * depth

result_1 = find_volume_1(10, 5, 3, 2)

print(result_1)

def find_volume_2(length=1, width=1, height=1, depth=1):
    return length * width * height * depth, width, 'hola'

result_2, width, text = find_volume_2(width=10)

print(result_2)
print(width)
print(text)