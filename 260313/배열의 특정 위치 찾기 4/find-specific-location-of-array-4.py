nums = list(map(int, input().split()))

cnt = 0
total = 0

for num in nums:
    if num == 0:
        break

    if num % 2 == 0:
        cnt += 1
        total += num


print(f"{cnt} {total}")