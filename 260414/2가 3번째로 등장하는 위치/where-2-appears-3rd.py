N = int(input())
nums = list(map(int, input().split()))

cnt = 0

for idx in range(N):
    if nums[idx] == 2:
        cnt += 1

    if cnt == 3:
        print(idx + 1)
        break