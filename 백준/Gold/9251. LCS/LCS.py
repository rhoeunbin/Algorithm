import pprint

w1 = input()
w2 = input()
len1, len2 = len(w1), len(w2) # 6

dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
# pprint.pprint(dp)

for i in range(1, len1 + 1) :
    for j in range(1, len2 + 1) :
        if w1[i - 1] == w2[j - 1] :
            dp[i][j] = dp[i - 1][j - 1] + 1
        else :
            dp[i][j] = max(dp[i - 1][j],dp[i][j - 1])
# pprint.pprint(dp)

print(dp[len1][len2])