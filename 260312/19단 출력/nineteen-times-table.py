cnt = 0

for i in range(1, 20):
    for j in range(1, 20):
        cnt += 1

        if cnt == 2 or j == 19:
            print(f"{i} * {j} = {i * j}", end = "\n")

            if cnt == 2 or j == 19:
                cnt = 0

        else:
            print(f"{i} * {j} = {i * j} /", end = " ")