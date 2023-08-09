import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dp = [0] * (10001)
dp[0] = 1
for i in range(1, 10001):
    dp[i] = (dp[i - 1] + dp[i - m]) % (1000000007)
print(dp[n])