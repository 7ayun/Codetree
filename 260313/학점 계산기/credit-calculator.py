N = int(input())
nums = list(map(float, input().split()))

nums = sum(nums)

avg = nums / N

print(f"{avg:.1f}")

if avg >= 4.0:
    print("Perfect")

elif avg >= 3.0:
    print("Good")

elif avg < 3.0:
    print("Poor")