Y = int(input())

if Y % 4 == 0:
    print('true')
else:
    if Y % 4 == 1 or (Y % 100 == 0 and Y % 400 != 0):
        print('false')