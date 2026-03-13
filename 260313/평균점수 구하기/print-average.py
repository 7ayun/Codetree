scores = list(map(float, input().split()))

scores = sum(scores)

avg = scores / 8

print(f"{avg:.1f}")