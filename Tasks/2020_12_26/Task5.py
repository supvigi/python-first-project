def func_1(x2, num2, pre_num2, z2, pre_pre_num2):
    z2 += 1
    num2 = pre_num2 + pre_pre_num2
    pre_pre_num2 = pre_num2
    pre_num2 = num2
    if z2 == x2:
        print("Your result is", num2)
        exit(0)
    else:
        func_1(x2, num2, pre_num2, z2, pre_pre_num2)


x = int(input("Put in the number X: "))
pre_x = 0
pre_pre_num1 = 1
pre_num1 = 1
num1 = 2
z = 0

if x == 1 or x == 2:
    print("Your result is 1")
else:
    func_1(x, num1, pre_num1, z, pre_pre_num1)
