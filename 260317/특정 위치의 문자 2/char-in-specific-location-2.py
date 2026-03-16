cha = list(map(str, input().split()))

result = []

for i, val in enumerate(cha):
    order = i + 1

    if order == 2 or order == 5 or order == 8:
        result.append(val)

print(*result)