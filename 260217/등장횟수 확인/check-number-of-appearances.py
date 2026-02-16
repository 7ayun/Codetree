nums = [int(input()) for _ in range(5)]

count = 0

for num in nums:
    if num % 2 == 0:
        count += 1

print(count)