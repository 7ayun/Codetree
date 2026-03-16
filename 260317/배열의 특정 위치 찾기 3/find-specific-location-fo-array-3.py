nums = list(map(int, input().split()))

check = []

total = 0

for num in nums:
    if num == 0:
        break

    check.append(num)

for _ in range(3):
    total += check.pop()

print(total)