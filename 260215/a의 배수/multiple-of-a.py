N, a = list(map(int, input().split()))

i = 1

while True:
    if i % a == 0:
        print(1)
    else:
        print(0)

    if i == N:
        break

    else:
        i += 1
    