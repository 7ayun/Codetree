N = int(input())
nums = [int(input()) for _ in range(N)]

total = 0
count = 0

for num in nums:
    total += num
    count += 1

avg = (total / count)

print(f'{total} {avg:.1f}')