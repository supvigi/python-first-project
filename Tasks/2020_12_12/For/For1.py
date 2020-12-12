qty = int(input("Put in the quantity of lines: "))
symbol = str(input("Put in the symbol that you want to clone: "))
symbolQty = int(input("Put in the quantity of symbols: "))

for ln in range(1, qty + 1):
    print(ln, str(symbol * symbolQty))

print("Press Ctrl + LShift + R to restart the program")
