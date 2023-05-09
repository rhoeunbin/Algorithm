import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
for i in range(1, n + 1):
    # 상담을 완료하는 데 걸리는 기간 / 상담을 했을 때 받을 수 있는 금액
    t, p = map(int, input().split())
    # print(dp)
    dp[i] = max(dp[i - 1], dp[i])
    # print(dp)
    endate = i + t - 1
    if endate <= n:
        dp[endate] = max(dp[i - 1] + p, dp[endate])

print(max(dp))