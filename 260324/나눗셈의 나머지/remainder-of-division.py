A, B = list(map(int, input().split()))

count = [0] * 10

while True:
    if A <= 1:
        break
    
    count[A % B] += 1
    A = A // B 

result = 0

for idx in range(len(count)):
    result += count[idx] ** 2
    
print(result)