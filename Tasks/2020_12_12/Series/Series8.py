count = 0
lst = []

while True:
    new_num = input("Put in the new number between -100 and 100 in the list or "
                    "word \"stop\" to stop adding elements to the list: ")

    if new_num == "stop" or new_num == "Stop":
        break

    if -100 < int(new_num) < 100:
        pass
    else:
        print("OOPS")
        exit(1)

    lst.append(int(new_num))

print("Before", lst)

lst2 = []

for x in lst:
    if x % 2 == 0:
        count += 1
        lst2.append(x)

print("Quantity of elements in the list is", count)
print("After", lst2)
