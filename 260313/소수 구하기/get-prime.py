N = int(input())

for i in range(1, N + 1):
    current_cnt = 0

    for j in range(1, i + 1):
        if i % j == 0:
            current_cnt += 1

    if current_cnt == 2:
        print(i, end = " ")