n = int(input())

dp = [0]*(n)
child = []
for i in range(n):
    child.append(int(input()))
    for j in range(i):
        if child[i] > child[j]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1

print(n - max(dp))