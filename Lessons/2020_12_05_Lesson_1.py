FriendlyInterface = "The heaviest coin is"

print("Don't forget to put cursor on the line of console!")

first = int(input("Write the weight of the first coin: "))
second = int(input("Write the weight of the second coin: "))
third = int(input("Write the weight of the third coin: "))

if second > first and second > third:
    print(FriendlyInterface, "second, its weight is", second)

if first > second and first > third:
    print(FriendlyInterface, "first, its weight is", first)

if third > first and third > second:
    print(FriendlyInterface, "third, its weight is", third)

print("Please, push Ctrl + LShift + R to compare another three coins")
