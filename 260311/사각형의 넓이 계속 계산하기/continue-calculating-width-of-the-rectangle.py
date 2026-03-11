while True:
    try:
        line = input().split()

        if not line:
            break

        r, c, s = line

        area = int(r) * int(c)
        print(area)

        if s == "C":
            break

    except(EOFError, ValueError):
        break