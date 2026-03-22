N = int(input())

nums = list(map(int, input().split()))

count = [0] * 10

for num in nums:
    count[num] += 1
    
for idx in range(1, 10):
    print(count[idx])
    