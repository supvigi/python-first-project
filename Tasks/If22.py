print("Write the coordinates of your point:")
x = int(input("Write the OX: "))
y = int(input("Write the OY: "))
quarter = 0

if x > 0 and y > 0:
    quarter = 1
elif x < 0 and y < 0:
    quarter = 3
elif x < 0 and y > 0:
    quarter = 2
elif x > 0 and y < 0:
    quarter = 4
elif x == 0 and y == 0:
    print("You are in the middle of nowhere!")
else:
    print("You are on the axis")

print("Your quarter is", quarter)
