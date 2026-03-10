N = int(input())

result = N

for i in range(1, 101):
    result //= i

    if result <= 1:
        print(i)
        break