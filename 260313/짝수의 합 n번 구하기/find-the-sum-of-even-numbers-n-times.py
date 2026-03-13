N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

for idx in range(N):
    current_sum = 0

    for i in range(nums[idx][0], nums[idx][1] + 1):
        if i % 2 == 0:
            current_sum += i

    print(current_sum)