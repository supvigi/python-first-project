number = int(input("Put in the number: "))

if 1 <= number <= 999:
    pass
else:
    print("Wrong number!")
    exit(1)

if number // 100 > 0:
    digits = "three-digits"
elif number // 10 > 0:
    digits = "two-digits"
else:
    digits = "one-digit"

if number % 2 == 1:
    odd_or_not = "odd"
else:
    odd_or_not = "even"

print(digits, odd_or_not, "number")
