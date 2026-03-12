N = int(input())

for i in range(1, N + 1):
    count = N - i + 1
    
    for j in range(1, count + 1):
        print(f"{i} * {j} = {i * j}", end="")

        if j < count:
            print(" / ", end="")

    print()