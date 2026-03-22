nums = list(map(int, input().split()))

counter = [0] * 7

for num in nums:
    counter[num] += 1
    
for idx in range(1, 7):
    print(f"{idx} - {counter[idx]}")