N = int(input())

for i in range(N):
    for _ in range((N * 2) - ((i + 1) * 2)):
        print(" ", end = "")

    for _ in range(i + 1):
        print("@", end = " ")
    print()
    
for i in range(N - 1, 0, -1):
    for _ in range(i):
        print("@", end = " ")
    print()
    