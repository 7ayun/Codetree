N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

for idx in range(N):
    total = 1

    for j in range(nums[idx][0], nums[idx][1] + 1):
        total *= j

    print(total)