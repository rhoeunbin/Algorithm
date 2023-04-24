n = int(input())
child = list(map(int, input().split()))
dp = [0] * (n+1)
LIS = 0
 
for i in child:
    dp[i] = dp[i - 1] + 1
    LIS = max(LIS, dp[i])
print(n - LIS)