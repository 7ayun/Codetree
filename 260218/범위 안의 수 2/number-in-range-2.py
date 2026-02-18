nums = [int(input()) for _ in range(10)]

total = 0
count = 0

for num in nums:
    if 0 <= num <= 200:
        total += num
        count += 1

avg = (total / count)

print(f'{total} {avg:.1f}')