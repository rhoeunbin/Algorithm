M = int(input())
N = int(input())

decimal = []
for num in range(M, N+1):
    cnt = 0 # 나눠지는 수가 있으면 카운트
    if num > 1: # 1은 소수가 아니므로 제외
        for x in range(2, num): # 2~num에서 나눠지는 수를 찾는다
            if num % x == 0: # 약수가 존재하므로 소수가 아님
                cnt += 1
                break  # 더이상 검사할 필요가 없으므로 멈춤
        if cnt == 0: # 나눠지는 수가 없으면 소수
            decimal.append(num)

if len(decimal) > 0:
    print(sum(decimal))
    print(min(decimal))
else:
    print(-1)