sum = 0
cnt = 0

while True:
    
    try:
        age = int(input())

        if not 20 <= age <= 29:
            if cnt > 0:
                print(f"{sum / cnt:.2f}")
            
            else:
                print(0.00)
            
            break
            
        sum += age
        cnt += 1

    except EOFError:
        if cnt > 0:
            print(f"{sum / cnt:.2f}")
        break

    except ValueError:
        break