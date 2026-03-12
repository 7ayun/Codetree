N = int(input())

for i in range(N):
    for _ in range(i):
        print("  ", end = "")

    for _ in range((N - i) * 2 -1):
        print("*", end = " ")
    print()

for i in range(N - 1):
    for _ in range(N - 2 - i):
        print("  ", end = "")

    for _ in range((i * 2) + 3):
        print("*", end = " ")
    print()
