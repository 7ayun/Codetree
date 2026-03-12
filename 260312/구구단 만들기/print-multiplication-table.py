A, B = list(map(int, input().split()))

for i in range(1, 10):
    for j in range(B, A - 1, -1):
        if j % 2 == 0:
            if j > A:
                print(f"{j} * {i} = {j * i}", end = " / ")

            else:
                print(f"{j} * {i} = {j * i}", end = "")

    print()