N = int(input())

for temp in range(1, N + 1):
    if temp % 2 == 0 or temp % 3 == 0:
        print(1, end = ' ')
    else:
        print(0, end = ' ')