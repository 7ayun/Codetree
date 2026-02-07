a, b = map(int, input().split())

if 90 <= a and 95 <= b:
    print(100000)
elif 90 <= a and 90 <= b:
    print(50000)
else:
    print(0)
