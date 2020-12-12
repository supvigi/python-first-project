x1 = int(input("Put in the first x : "))
y1 = int(input("Put in the first y : "))
x2 = int(input("Put in the second x: "))
y2 = int(input("Put in the second y: "))
x3 = int(input("Put in the third x: "))
y3 = int(input("Put in the third y: "))
x4 = None
y4 = None

if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
elif x2 == x3:
    x4 = x1
else:
    print("Введённые координаты некорректны")
    exit(1)

if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
elif y2 == y3:
    y4 = y1
else:
    print("Введённые координаты некорректны")
    exit(1)

print("Координаты четвёртой вершины равны (" + str(x4) + ", " + str(y4) + ")")
