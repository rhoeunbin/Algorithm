n = int(input())
num = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = num[0]
# print(num, dp)

for i in range(n):
    dp[i] = max(dp[i - 1] + num[i], num[i])
    # print(dp)
print(max(dp))