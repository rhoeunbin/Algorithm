import sys
input = sys.stdin.readline

schedule = []

n = int(input())
for i in range(n):
    schedule.append(list(map(int, input().split())))

dp = [0] * (n + 1)

for i in range(n):
    for j in range(i + schedule[i][0], n + 1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]

print(max(dp))