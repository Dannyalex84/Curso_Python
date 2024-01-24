def sum_with_range(min, max):
    print(min, max)
    sum = 0
    for x in range(min, max):
        sum += x
    return sum
        
result = sum_with_range(1, 10)
print(result)
result_2 = sum_with_range(result, result + 10)
print(result_2)
# sum_with_range(20, 30)
# sum_with_range(1, 100)

def calculator(num_1, num_2, op):
    result = 0

    if op == "+":
        result = num_1 + num_2

    elif op == "-":
        result = num_1 - num_2

    elif op == "*":
        result = num_1 * num_2

    elif op == "/":
        result = num_1 / num_2

    print(f"{num_1} {op} {num_2} = {result}")

if __name__ == '__main__':
  list_op = ("+", "-", "*", "/")
  op = str(input(f'choose operator with symbol {list_op}: '))
  num_1 = int(input('Choose number: '))
  num_2 = int(input('Choose other number: '))
  calculator(num_1, num_2, op)