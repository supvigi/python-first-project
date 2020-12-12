a = int(input("Write the A: "))
b = int(input("Write the B: "))
c = int(input("Write the C: "))

if a < b < c or a > b > c:
    print("B is the middle number")
elif b < a < c or c < a < c:
    print("A is the middle number")
elif b < c < a or a < c < b:
    print("C is the middle number")
else:
    print("Looks like some of the numbers are equal")