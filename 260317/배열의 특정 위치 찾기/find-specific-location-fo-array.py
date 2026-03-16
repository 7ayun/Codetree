nums = list(map(int, input().split()))

first_total = 0
second_total = 0
second_cnt = 0

for idx in range(len(nums)):
    if idx % 2 != 0:
        first_total += nums[idx]

for num in nums:
    if num % 3 == 0:
        second_total += num
        second_cnt += 1

second_avg = second_total / second_cnt

print(f"{first_total} {second_avg:.1f}")