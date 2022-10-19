n = int(input())

result = 1
if n > 0:
    for i in range(1, n+1):
        result *= i # 계속 곱하기
print(result)