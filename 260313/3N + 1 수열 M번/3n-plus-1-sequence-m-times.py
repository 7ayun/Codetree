M = int(input())

for i in range(M):
    cnt = 0
    N = int(input())

    while True:
        if N == 1:
            print(cnt)
            break

        elif N % 2 == 0:
            N /= 2

        elif N % 2 != 0:
            N *= 3
            N += 1

        cnt += 1