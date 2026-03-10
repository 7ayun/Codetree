count = 0

while True:
    N = int(input())

    if N % 2 != 0:
        continue

    if N % 2 == 0:
        result = N // 2
        print(result)
        count += 1
        
        if count == 3:
            break