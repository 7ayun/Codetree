N = int(input())

cnt = 65

for i in range(N, 0, -1):
    start_value = (N - i) * 2

    for j in range(start_value):
        print(" ", end = "")

    for _ in range(i):
        if cnt > 90:
            cnt = 65
        print(chr(cnt), end = " ")
        cnt += 1

    print()