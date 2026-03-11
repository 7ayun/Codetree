N = int(input())

check = True

for i in range(2, N + 1):
    if i != N:
        if N % 1 == 0 and N % i == 0:
            check = False

if check:
    print("P")
else:
    print("C")