z = 0
sign = "_"
sentence = str(input("Put in the sentence: "))
lst = list(sentence)

for x in lst:
    if x == " ":
        lst.remove(x)
        lst.insert(z, sign)

    z += 1

convert = "".join(map(str, lst))

print(convert)
