def gcf(num_1, num_2, small_one, half_small_one, i2, lst2, big_one):
    if i2 > half_small_one:
        if big_one / small_one % 1 == 0:
            print("Your GCF is", small_one)
            exit(0)
        else:
            lst2.sort()
            print("Your GCF is", lst2[len(lst2)])
            exit(0)
    if num_1 / i2 == int and num_2 / i2 == int:
        lst2.append(i2)
    else:
        i2 += 1
        gcf(num_1, num_2, small_one, half_small_one, i2, lst2, big_one)


number1 = int(input("Put in the first number: "))
number2 = int(input("Put in the second number: "))
i = 1
lst = []

if number2 < number1:
    smaller_one = number2
    bigger_one = number1
else:
    smaller_one = number1
    bigger_one = number2

half_smaller_one = smaller_one / 2

gcf(number1, number2, smaller_one, half_smaller_one, i, lst, bigger_one)
