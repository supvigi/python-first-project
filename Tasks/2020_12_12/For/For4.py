z = 0
pre_x = None
sentence = str(input("Put in the sentence: "))
lst = list(sentence)

for x in lst:
    if x == " " and x == pre_x:
        lst.pop(z)
        lst.insert(z, None)

    pre_x = x
    z += 1

while lst.count(None) > 0:
    lst.remove(None)

lst_converted = "".join(map(str, lst))

print(lst_converted)
