N = int(input())
scores = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

for idx in range(N):
    avg = sum(scores[idx]) / 4
    if avg >= 60:
        print("pass")
        cnt += 1

    else:
        print("fail")

print(cnt)