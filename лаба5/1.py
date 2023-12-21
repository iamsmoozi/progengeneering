import math


def funcx(z):
    return (z * z) + 3


def funcy():
    return math.sin(4)


def func(x, y):
    return x + y


res = func(funcx(2), funcy())
print(res)

