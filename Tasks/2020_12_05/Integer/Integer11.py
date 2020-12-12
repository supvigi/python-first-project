number = int(input("Write the number: "))

a = number // 100
b = number // 10 % 10
c = number % 10

print("The sum of digits in your number is", a + b + c)
print("The result of multiplying your digits is", a * b * c)