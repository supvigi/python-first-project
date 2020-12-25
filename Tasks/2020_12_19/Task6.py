def calc(a2, b2, op2):
    if op2 == 1:
        return "Your result is", a2 - b2
    elif op2 == 2:
        return "Your result is", a2 * b2
    elif op2 == 3:
        return "Your result is", a2 / b2
    else:
        return "Your result is", a2 + b2


a = int(input("Put in the A: "))
b = int(input("Put in the b2: "))
op = int(input("Put in the op2. Warning, 1 = minus, 2 = multiply, 3 = divide, other = plus: "))

print(calc(a, b, op))
