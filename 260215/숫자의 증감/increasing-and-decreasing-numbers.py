C, N = list(map(str, input().split()))

if C == 'A':
    for temp in range(1, int(N) + 1):
        print(temp, end = ' ')

if C == 'D':
    for temp in range(int(N), 0, -1):
        print(temp, end = ' ')