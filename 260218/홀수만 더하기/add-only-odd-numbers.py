N = int(input())
nums = [int(input()) for _ in range(N)]

total = 0

for num in nums:
    if num % 2 == 1 and num % 3 == 0:
        total += num

print(total)