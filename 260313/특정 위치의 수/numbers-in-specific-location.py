nums = list(map(int, input().split()))

cnt = 1
total = 0

for num in nums:
    if cnt == 3 or cnt == 5 or cnt == 10:
        total += num

    cnt += 1

print(total)