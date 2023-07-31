n = int(input())
m = int(input())
vip = [int(input()) for _ in range(m)]

dp = [0] * (n + 1)
'''
n = 1 : 1 => 1
n = 2 : 12 21 => 2
n = 3 : 123 213 132 => 3
n = 4 : 1234 2134 1324 (n = 3에 4를 붙임) 2143 1243 => 5
n = 5 : 12345 12435 13245 21345 21435 (n = 4에 5를 붙임)  21354 12354 13254 => 8
'''
# 123 56 89에 해당하는 dp[3] * dp[2] * dp[2] 가짓수
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

ans = 1
cnt = []
cur = 0
for i in range(1, n + 1):
    if i in vip:
        ans *= dp[cur]
        cur = 0
    else:
        cur += 1
ans *= dp[cur]

print(ans)
