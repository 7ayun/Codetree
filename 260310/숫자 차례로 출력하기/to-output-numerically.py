n = int(input())

# Please write your code here.

def print_nums(N):
    if N == n + 1:
        print()
        return

    print(N, end = ' ')
    print_nums(N + 1)
    print(N, end = ' ')

print_nums(1)