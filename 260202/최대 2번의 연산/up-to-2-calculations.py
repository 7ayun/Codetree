a = int(input())

if a % 2 == 0:
    a = (a / 2)

if a % 2 == 1:
    a = int((a + 1) / 2)

print(int(a))