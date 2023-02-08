import sys
INF = sys.maxsize #  최솟값 변수 초기화 (INF)

n = int(input())
liquid = list(map(int, input().split()))

liquid.sort()

start = 0
end = n - 1

min_val = INF
answer = []

while start < end:
    total = liquid[start] + liquid[end]
    # 두 용액의 합이 0과 가장 가까운 용액을 정답에 담아주기
    if abs(total) < min_val:
        min_val = abs(total)
        answer = (liquid[start], liquid[end])

    # 0에 가까워지기 위해서
    if total < 0: # 합이 음수 
        start += 1
    else:
        end -= 1

print(*answer)