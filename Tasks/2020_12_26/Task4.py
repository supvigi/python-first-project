def func_1(x2, z2, result2):
    z2 += 1
    if z2 == x2:
        print("Your result is", result2)
        exit(0)
    result2 *= 2
    func_1(x2, z2, result2)


x = int(input("Put in the power: "))
z = 0
result = 2

func_1(x, z, result)
