A, B = list(map(int, input().split()))

max_num = max(A, B)
min_num = min(A, B)

for temp in range(max_num, min_num - 1, -1):
    print(temp, end = " ")