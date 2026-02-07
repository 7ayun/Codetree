user_1 = input().split()
user_2 = input().split()
user_3 = input().split()

cnt = 0

if 'Y' in user_1:
    if int(user_1[1]) >= 37:
        cnt += 1
    else:
        pass
elif 'N' in user_1:
    if int(user_1[1]) >= 37:
        pass
    else:
        pass

if 'Y' in user_2:
    if int(user_2[1]) >= 37:
        cnt += 1
    else:
        pass
elif 'N' in user_2:
    if int(user_2[1]) >= 37:
        pass
    else:
        pass

if 'Y' in user_3:
    if int(user_3[1]) >= 37:
        cnt += 1
    else:
        pass
elif 'N' in user_3:
    if int(user_3[1]) >= 37:
        pass
    else:
        pass

if cnt >= 2:
    print('E')
else:
    print('N')