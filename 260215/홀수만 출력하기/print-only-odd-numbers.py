N = int(input())

for _ in range(N):
    s = int(input())
    if s % 2 == 1 and s % 3 == 0:
        print(s)