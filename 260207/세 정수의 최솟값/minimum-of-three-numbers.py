a, b, c = map(int, input().split())

min_value = a

if min_value > b:
    min_value = b

if min_value > c:
    min_value = c

print(min_value)
