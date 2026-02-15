N = int(input())

score = N

while True:
    if score >= 90:
        print('A', end = ' ')
    elif score >= 80:
        print('B', end = ' ')
    elif score >= 70:
        print('C', end = ' ')
    elif score >= 60:
        print('D', end = ' ')
    else:
        print('F', end = ' ')

    if score == 100:
        break
    else:
        score += 1