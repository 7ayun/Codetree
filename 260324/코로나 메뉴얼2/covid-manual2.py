member = [list(map(str, input().split())) for _ in range(3)]

count = [0] * 4

for idx in range(len(member)):
    if member[idx][0] == "Y":
        if int(member[idx][1]) >= 37:
            count[0] += 1
            
        else:
            count[2] += 1
            
    if member[idx][0] == "N":
        if int(member[idx][1]) >= 37:
            count[1] += 1
            
        else:
            count[3] += 1
            
if count[0] >= 2:
    print(*count, "E") 

else:
    print(*count)