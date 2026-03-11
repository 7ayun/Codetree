N = int(input())

for i in range(N):
    print("  " * (N - 1 - i), end="")

    for _ in range(i * 2 + 1):
        print("*", end = " ")
    print()