nums = [int(input()) for _ in range(10)]

count_3 = 0
count_5 = 0

for num in nums:
    if num % 3 == 0:
        count_3 += 1
    
for num in nums:    
    if num % 5 == 0:
            count_5 += 1

print(count_3, count_5)