a, b, c = map(int, input().split())

min_value = a

if  min_value > b:
    min_value = b

elif min_value > c:
    min_value = c

if min_value == a:
    print(1, end = ' ')
else:
    print(0, end = ' ')

if a == b == c:
    print(1, end = ' ')
else:
    print(0, end = ' ')