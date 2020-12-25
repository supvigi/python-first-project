import math


def func_1(a2, h2):
    b = math.sqrt(a2 ** 2 + h2 ** 2)
    return b


a = int(input("Put in the A: "))
h = int(input("Put in the H: "))

print(func_1(a, h))
