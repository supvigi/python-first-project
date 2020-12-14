a = int(input("Put in the A: "))
b = int(input("Put in  the B: "))
c = int(input("Put in the C: "))
lst = [a, b, c]
ggl = 0

for x in lst:
    if ggl < x:
        ggl = x

print("The biggest number in the list is", ggl)
