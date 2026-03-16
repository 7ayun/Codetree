nums = list(map(int, input().split()))

even = 0
odd = 0

for i, num in enumerate(nums):
    order = i + 1

    if order % 2 != 0:
        odd += num

    if order % 2 == 0:
        even += num

result = max(even, odd) - min(even, odd)

print(result)