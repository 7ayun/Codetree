user_1_age, user_1_gender = map(str, input().split())
user_2_age, user_2_gender = map(str, input().split())

if (int(user_1_age) >= 19 and user_1_gender == 'M') or (int(user_2_age) >= 19 and user_2_gender == 'M'):
    print(1)
else:
    print(0)
