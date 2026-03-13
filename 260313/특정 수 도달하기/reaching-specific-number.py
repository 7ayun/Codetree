nums = list(map(int, input().split()))

cnt = 0
total = 0

for num in nums:
    if num >= 250:
        break

    total += num
    cnt += 1

avg = (total / cnt)

print(f"{total} {avg:.1f}")