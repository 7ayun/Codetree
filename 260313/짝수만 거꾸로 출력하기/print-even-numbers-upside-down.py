N = int(input())
nums = list(map(int, input().split()))

new_nums = []

for num in nums:
    if num % 2 == 0:
        new_nums.append(num)

new_nums.reverse()

print(*new_nums)