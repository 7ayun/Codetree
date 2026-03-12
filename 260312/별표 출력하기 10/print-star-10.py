N = int(input())

for i in range(1, N + 1):
    for _ in range(i):
        print("*", end = " ")
    print()
    
    for _ in range(N + 1 - i):
        print("*", end = " ")
    
    print()