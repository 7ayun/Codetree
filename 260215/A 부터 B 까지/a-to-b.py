A, B = list(map(int, input().split()))

result = A

while True:
    if result > B:
        break

    if result % 2 == 1:
        print(result, end = ' ')
        result *= 2
    elif result % 2 == 0:
        print(result, end = ' ')
        result += 3
