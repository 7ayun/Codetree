nums = list(map(int, input().split()))
a, b, c = nums

check = False

for i in range(a, b + 1):
    if i % c == 0:
        check = True

if check:
    print("YES")
else:
    print("NO")