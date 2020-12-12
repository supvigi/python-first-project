a = 0

for i in range(1, 100 + 1, 1):
    print(i)
    a += i
print(a)


z = 0
length = 10
p = int(input("Put in the P: "))

if 0 < p < 50:
    pass
else:
    print("Error!")
    exit(1)

while length <= 200:
    length += length * p / 100
    z += 1
print("The length is", length)
print("The sum of days is", z)


n = int(input("Put in the two-digits number: "))

if n // 100 == 5:
    print("Yes")
elif n % 10 == 5:
    print("Yes")
else:
    print("No")


a = [1, 2, 3, 4, 5]
x = 4
print(a[3] + 5)
print(x + 5)


a = [1, [1, [1, [1, 2, 3], 3], 3], 3]
print(a[1][1][1][1])
