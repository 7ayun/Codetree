start, end = map(int, input().split())

# Please write your code here.

cnt = 0 

for num in range(start, end + 1):
    current_sum = 0

    for i in range(1, num):
        if num % i == 0:
            current_sum += i

    if current_sum == num:
        cnt += 1

print(cnt)