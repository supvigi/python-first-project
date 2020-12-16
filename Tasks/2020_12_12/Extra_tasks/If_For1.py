triangle_exist = 0
triangle_not_exist = 0

for x in range(1, 4):
    locals()['lst{}'.format(x)] = []
    while len(locals()['lst{}'.format(x)]) != 10:
        new_num = input("Put in the new positive number in the list or "
                        "word \"stop\" to stop adding elements to the list of the {} side: ".format(x))

        if new_num == "stop" or new_num == "Stop":
            break

        if int(new_num) > 0:
            pass
        else:
            print("OOPS")
            exit(1)

        locals()['lst{}'.format(x)].append(int(new_num))


for side1 in lst1:
    for side2 in lst2:
        for side3 in lst3:
            if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
                print("Triangle with sides: {}, {}, {} exists".format(side1, side2, side3))
                triangle_exist += 1
            else:
                print("There is no triangle with sides: {}, {}, {}".format(side1, side2, side3))
                triangle_not_exist += 1

print("Total: there is {} triangles that don't exist, "
      "and {} triangles that exist".format(triangle_not_exist, triangle_exist))

print(locals())
print(globals())
