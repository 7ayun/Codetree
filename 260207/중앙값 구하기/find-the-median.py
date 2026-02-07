A, B, C = map(int, input().split())

if A > B and B > C:
    print(B)
else:
    if A < B and B < C:
        print(B)

if B > A and A > C:
    print(A)
else:
    if B < A and A < C:
        print(A)

if A > C and C > B:
    print(C)
else:
    if A < C and C < B:
        print(C)