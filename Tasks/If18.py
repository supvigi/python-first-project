a = int(input("Write the A: "))
b = int(input("Write the B: "))
c = int(input("Write the C: "))
aln = 1
bln = 2
cln = 3

if a == b and b != c:
    print("The C is not equal to others. Its number in line is", cln)
elif a == c and c != b:
    print("The B is not equal to others. Its number in line is", bln)
elif b == c and a != c:
    print("The A is not equal to others. Its number in line is", aln)
else:
    print("Error!")