N = int(input())

cnt = 65

for i in range(1, N + 1):
    for j in range(i):
        if cnt > 90:
            cnt = 65
        print(chr(cnt), end = "")
        cnt += 1

    print()