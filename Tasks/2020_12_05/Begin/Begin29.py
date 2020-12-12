pi = 3.14
alpha = int(input("Put in the alpha, please: "))

if 0 < alpha < 360:
    print("Your angle is", round(pi / 180 * alpha, 2), "radians")
else:
    print("You have to write the number between 0 and 360.")