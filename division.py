from asyncio import run


def make_division_by(n):
    return lambda x: x/n


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))    # 6.0
    division_by_5 = make_division_by(5)
    print(division_by_5(100))   #20.0
    division_by_18 = make_division_by(18)
    print(division_by_18(54))   #3.0


if __name__ == "__main__":
    run()

