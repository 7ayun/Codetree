n = int(input())

# Please write your code here.

def print_star(N):
    if N == n + 1:
        return

    print("*" * N)
    print_star(N + 1)

print_star(1)