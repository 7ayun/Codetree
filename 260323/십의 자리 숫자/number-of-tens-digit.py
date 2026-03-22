nums = list(map(int, input().split()))

counter = [0] * 10

for num in nums:
    if num == 0:
        break
    
    i = num // 10
    
    counter[i] += 1
    
for idx in range(1, 10):
    print(f"{idx} - {counter[idx]}")
    