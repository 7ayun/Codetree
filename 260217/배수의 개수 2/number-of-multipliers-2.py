nums = [int(input()) for _ in range(10)]

count = 0

for num in nums:
    if num % 2 == 1:
        count += 1

print(count) 