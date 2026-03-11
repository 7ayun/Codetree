nums = list(map(int, input().split()))
a, b, c = nums

check = True

for i in range(a, b + 1):
    if  i % c == 0:
        check = False
        break

if check:
    print("YES")
else:
    print("NO")