"""
    Simple timing example..
"""

def foo(x):
    if x < 0:
        raise ValueError('error, ouch', x)

try:
    foo(-1)
except Exception as ex:
    print('error occurred')
    print(ex)
    print(type(ex).__name__)
    print(f"negative arg: {ex.args[1]}")

print(type(10).__name__)

def gcd(a, b):
    if b == 0:
       return a
    else:
       return gcd(b, a % b)

print(gcd(100, 11))

import time

def time_decorator(fn):
    def func(x):
        start = time.time()
        x = fn(x)
        end = time.time()
        return x, end-start
    return func

@time_decorator
def sum_of_n_2(n):
    the_sum = 0

    for i in range(1, n+1):
        the_sum += i

    return the_sum

@time_decorator
def f2(n):
    return sum(range(1,n+1))

print(sum_of_n_2(100))
print(f2(100))