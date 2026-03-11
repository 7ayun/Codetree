age_avg = 0
count = 0

while True:
    age = int(input())

    if age > 29:
        print(f"{age_avg / count:.2f}")
        break

    age_avg += age
    count += 1
