N = int(input())

def prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

result = 0

for x in range(N, 1000001):
    if x == 1:
        continue
    if str(x) == str(x)[::-1]:
        if prime(x) == True:
            result = x
            break

# 구글링
if result == 0: # 입력값이 만약 최대 값 100만일 경우
    result = 1003001 # 100만 이상이면서 팰림드롬 및 소수일 경우를 적용 1003001이 팰린드롬 수
print(result)