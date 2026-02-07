a, b, c = map(int, input().split())

max_value = a

if max_value < b:
    max_value = b

if max_value < c:
    max_value = c

print(max_value)