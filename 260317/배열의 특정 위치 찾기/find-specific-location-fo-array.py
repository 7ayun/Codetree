nums = list(map(int, input().split()))

even_sum = 0
triple_sum = 0
triple_cnt = 0

for i, val in enumerate(nums):
    order = i + 1

    if order % 2 == 0:
        even_sum += val

    if order % 3 == 0:
        triple_sum += val
        triple_cnt += 1

triple_avg = triple_sum / triple_cnt

print(f"{even_sum} {triple_avg:.1f}")