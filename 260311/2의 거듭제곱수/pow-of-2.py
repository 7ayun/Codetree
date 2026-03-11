N = int(input())

x = 1

while True:
    if 2 ** x == N:
        print(x)
        break

    x += 1