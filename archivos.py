def read():
    numbers =[]
    with open("./Archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Luima", "Rubiela", "María", "Karina", "Carol", "Dayanna", "Danny", "Alexander", "Patricia", "Anthuan", "Isaac", "Diego"]
    with open("./Archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    write()


if __name__ == '__main__':
    run()