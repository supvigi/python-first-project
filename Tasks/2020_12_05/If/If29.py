number = int(input("Put in the number: "))

if number > 0:
    plus_or_not = "positive"
elif number < 0:
    plus_or_not = "negative"
else:
    plus_or_not = "zero"

if number % 2 == 1:
    odd_or_not = "odd"
else:
    odd_or_not = "even"

print(plus_or_not, odd_or_not, "number")
