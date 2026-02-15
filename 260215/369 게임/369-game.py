N = int(input().strip())

out = []
for i in range(1, N + 1):
    s = str(i)
    if i % 3 == 0 or ('3' in s) or ('6' in s) or ('9' in s):
        out.append('0')
    else:
        out.append(s)

print(' '.join(out))
