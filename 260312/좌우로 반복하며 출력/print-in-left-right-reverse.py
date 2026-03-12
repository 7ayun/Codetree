N = int(input())

for i in range(1, N + 1):
    if i % 2 != 0:
        for j in range(N):
            print(j + 1, end = "")

    else:
        for j in range(N):
            print(N - j, end = "")

    print()