a, b, c = map(int, input().split())

if a == b or a == c:
    print(1, end = ' ')
else:
    print(0, end = ' ')

if a == b == c:
    print(1, end = ' ')
else:
    print(0, end = ' ')