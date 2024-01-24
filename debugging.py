def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Ingresa un número: "))
        
        if num < 0:
            raise Exception("Número negativo no es válido")
        print(divisors(num))
        print("Termino mi programa")
    except ValueError:
        print("Debes ingresar un número")
    except Exception:
        print("El número no puede ser negativo")


if __name__ == '__main__':
    run()