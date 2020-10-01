"""
    Simple timing example..
"""
from typing import Tuple
from timeit import time_decorator


def foo(x):
    if x < 0:
        raise ValueError('error, ouch', x)


try:
    foo(-1)
except Exception as ex:
    print('error occurred')
    print(ex)
    print(type(ex).__name__)
    print(f"negative arg: '{ex.args[0]}', {ex.args[1]}")

print(type(10).__name__)


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(100, 11))


@time_decorator
def sum_of_n_2(n):
    the_sum = 0

    for i in range(1, n + 1):
        the_sum += i

    return the_sum


@time_decorator
def f2(n):
    return sum(range(1, n + 1))


@time_decorator
def make_list1(n):
    x = []
    for i in range(1, n + 1):
        x.append(i)
    return x


@time_decorator
def make_list2(n):
    return list(range(1, n + 1))


@time_decorator
def make_list3(n):
    return [i for i in range(1, n + 1)]


# print(sum_of_n_2(10000))
# print(f2(10000))

print(make_list1(10))
print(make_list2(10))
print(make_list3(10))
