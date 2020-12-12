number = int(input("Write the number: "))

a = str(number // 100)
b = str(number // 10 % 10)
c = str(number % 10)

print("Your mirror number is", c + b + a)