n = int(input("Put in the N: "))
result = 1.1

pre_result = result
result += 0.1
print(result)
print(pre_result)

answer = 0

for x in range(n):
    pre_result = result
    result += 0.1
    answer = pre_result + result

print(answer)
