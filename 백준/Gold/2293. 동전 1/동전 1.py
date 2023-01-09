n, k = map(int, input().split())

coins = [int(input()) for i in range(n)]
# for i in range(n):
#     coins.append(int(input()))
# coins.sort()

dp = [0] * (k + 1) # 경우의 수를 저장할 리스트
dp[0] = 1 # 0원인 경우는 없지만, 이후의 계산을 위해 1로 지정한다.
# = dp[k -k] 합이 k가 되게 만들 때 k원짜리 동전 하나만 쓰는 경우
# dp [k] = 합이 k가 되는 경우의 수

for c in coins:
    for i in range(c, k + 1):
        dp[i] += dp[i - c] # dp [4] (1,2 원으로 4 만듦) = dp[4] (원래 1원으로만 4를 만듦) + DP[4 - 2] (1, 2 원으로 2를 만드는 경우의 수, 2원만 추가해주면 4가 되므로)

print(dp[k])