A, B = list(map(int, input().split()))

result = 1

for i in range(A, B + 1):
    result *= i

print(result)