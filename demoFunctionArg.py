from random import randint


def do_math(fn, op1, op2):
    return fn(op1, op2)


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def bad_counter():
    count = 0
    count += 1
    return count


def make_counter():
    count: int = [0]
    rand = [0, 0]

    def next_num():
        count[0] += 1
        rand[0] = randint(1, 100)
        rand[1] = rand[1] + count[0]
        return count[0], rand[1]

    return next_num


def main():
    print(do_math(add, 3, 4))
    print(do_math(mul, 3, 4))

    counter1 = make_counter()
    counter2 = make_counter()

    for i in range(1, 4):
        print("counter2", counter2())

    for i in range(1, 11):
        print(f"counter1:{counter1()}, counter2:{counter2()}")

    bad_count = bad_counter
    print(bad_count())
    print(bad_count())


if __name__ == "__main__":
    main()
