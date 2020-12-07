r1 = int(input("Write the length of the first radius: "))
r2 = int(input("Write the length of the second radius: "))
pi = 3.14
s2 = pi*r2**2
s1 = pi*r1**2

print("S2 =", s2)
print("S1 =", s1)

if s1 > s2:
    print("S3 =", s1 - s2)
elif s1 < s2:
    print("S3 =", s2 - s1)
else:
    print("S3 =", 0)