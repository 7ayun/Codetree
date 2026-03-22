nums = list(map(int, input().split()))

counter = [0] * 11

for num in nums:
    if num == 0:
        break
    
    i = num // 10
    
    counter[i] += 1
    
for idx in range(10, 0, -1):
    print(f"{idx * 10} - {counter[idx]}")