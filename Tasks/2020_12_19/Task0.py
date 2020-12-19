x = [1, 2, 3]
y = [6, 5, 4, 5, 8]

if len(x) > len(y):
    for i in range(len(y)):
        x[i] += y[i]
    print(x)
else:
    for i in range(len(x)):
        y[i] += x[i]
    print(y)
