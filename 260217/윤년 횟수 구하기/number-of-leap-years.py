N = int(input())

year_365 = 0
year_366 = 0

for i in range(1, N + 1):
    if i % 4 != 0 or (i % 100 == 0 and i % 400 != 0):
        year_365 += 1
    else:
        year_366 += 1

print(year_366)