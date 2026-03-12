n = int(input())

# Please write your code here.

for i in range(n):
    for _ in range(n - 1 - i):
        print(" ", end = "")

    for _ in range(i * 2 + 1):
        print("*", end = "")
    print()

for i in range(n - 1):
    for _ in range(i + 1):
        print(" ", end = "")
    
    for _ in range(n - (i * 2)):
        print("*", end = "")
    print()