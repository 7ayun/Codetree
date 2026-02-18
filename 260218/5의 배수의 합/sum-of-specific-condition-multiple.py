A, B = list(map(int, input().split()))

total = 0 

if A > B:
    A, B = B, A

for i in range(A, B + 1):
    if i % 5 == 0:
        total += i

print(total)