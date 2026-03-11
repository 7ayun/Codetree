N = int(input())

check = False

for i in range(2, N):
    if N % i == 0:
        check = True

if check:
    print("C")

else:
    print("N")