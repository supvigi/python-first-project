side1 = int(input("Put in the first side: "))
side2 = int(input("Put in the second side: "))
side3 = int(input("Put in the third side: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print('Triangle like that exists')
else:
    print('It is impossible to make a triangle like this')
