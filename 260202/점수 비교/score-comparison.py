A_mat, A_eng = map(int, input().split())
B_mat, B_eng = map(int, input().split())

if A_mat > B_mat and A_eng > B_eng:
    print(1)
else:
    print(0)