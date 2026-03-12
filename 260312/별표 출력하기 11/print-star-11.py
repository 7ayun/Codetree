N = int(input())

for i in range(1, N * 2 + 2):
    if i % 2 != 0:
        for _ in range(N * 2 + 1):
            print("* ", end = "")
        
    if i % 2 == 0:
        for _ in range(N + 1):
            print("*   ", end = "")
    
    print()