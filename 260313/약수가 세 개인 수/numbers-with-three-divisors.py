start, end = map(int, input().split())

# Please write your code here.

cnt = 0

for num in range(start, end + 1):
    current_cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            current_cnt += 1

    if current_cnt == 3:
        cnt += 1

print(cnt)