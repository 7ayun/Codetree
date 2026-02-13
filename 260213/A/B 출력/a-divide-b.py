# A와 B를 입력받습니다.
a, b = map(int, input().split())

# 1. 정수 부분 출력
print(a // b, end='.')

# 2. 소수점 아래 부분을 계산합니다.
# 나머지를 가지고 10을 곱해가며 한 자리씩 구하는 방식입니다.
remainder = a % b

for _ in range(20):
    remainder *= 10
    print(remainder // b, end='')
    remainder %= b