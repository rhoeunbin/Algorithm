import sys
input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    # 사탕 종류의 수 n과 상근이가 가지고 있는 돈의 양 m
    n, m = int(n), int(m * 100 + 0.5)

    if n == 0 and m == 0.00:
        break

    dp = [0] * (m + 1)
    for _ in range(n):
        c, p = map(float, input().split())
        #  각 사탕의 칼로리 c와 가격 p
        c, p = int(c), int(p * 100 + 0.5)

        for i in range(p, m + 1):
            dp[i] = max(dp[i], dp[i - p] + c)

    print(dp[m])