n = int(input())

classroom = 0
floor = 0
toilet = 0

for temp in range(1, n + 1):
    if temp % 2 == 0:
        classroom += 1
        if temp % 3 == 0:
            classroom -= 1
            floor += 1
            if temp % 12 == 0:
                floor -= 1
                toilet += 1

    elif temp % 3 == 0:
        floor += 1

print(classroom, floor, toilet)