check = True

while True:
    try:
        N = int(input())

        if N % 3 != 0:
            check = False
            break

    except EOFError:
        break

if check:
    print(1)
else:
    print(0)