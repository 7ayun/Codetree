N = int(input())

cnt = 2

for _ in range(N):
    for _ in range(N):
        if cnt == 10:
            cnt = 2

        print(cnt, end = " ")
        cnt += 2

    print()