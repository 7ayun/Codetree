while True:
    N = int(input())

    if N < 25:
        print("Higher")
    
    if N > 25:
        print("Lower")

    if N == 25:
        print("Good")
        break