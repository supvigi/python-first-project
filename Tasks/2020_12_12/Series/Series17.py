lst = []
b = float(input("Put in the number B: "))

while True:
    new_num = input("Put in the new number between -100 and 100 in the list or "
                    "word \"stop\" to stop adding elements to the list: ")

    if new_num == "stop" or new_num == "Stop":
        break

    if -100 < float(new_num) < 100:
        pass
    else:
        print("OOPS")
        exit(1)

    lst.append(float(new_num))

lst.append(b)
lst.sort()

print("Your list is", lst)
