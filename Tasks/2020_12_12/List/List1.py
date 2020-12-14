lst = []
mini = 100
ggl = -100
z = 0
z_ggl = 0
z_mini = 0

while True:
    new_num = input("Put in the new number between -100 and 100 in the list or "
                    "word \"Stop\" to stop adding elements to the list: ")

    if new_num == "stop" or new_num == "Stop":
        break

    if -100 < int(new_num) < 100:
        pass
    else:
        print("OOPS")
        exit(1)

    lst.append(int(new_num))

for x in lst:
    if ggl < x:
        ggl = x
        z_ggl = z
    if mini > x:
        mini = x
        z_mini = z
    z += 1

print("Before:", lst)

lst.remove(mini)
lst.insert(z_ggl, mini)
lst.remove(ggl)
lst.insert(z_mini, ggl)

print("After:", lst)
