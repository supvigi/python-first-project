import math


def is_square(k2):
    if math.sqrt(k2) % 2 == 0 or math.sqrt(k2) % 2 == 1:
        lst2.append(k2)
    else:
        pass


lst = []
lst2 = []

while len(lst) < 10:
    k = input("Put in the number to compare: ")
    if k == "stop" or k == "Stop":
        break
    else:
        pass
        is_square(int(k))

print("Your answer is", lst2)
