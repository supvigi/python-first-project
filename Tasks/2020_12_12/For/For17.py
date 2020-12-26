pre_a = 0
a_first = float(input("Put in the A: "))
a = a_first
n = int(input("Put in the N: "))
if n > 0:
    pass
else:
    print("YOU APE! IT'S SMALLER THAN 0!")
    exit(1)

for x in range(n):
    a *= a_first

print(a + 1)
