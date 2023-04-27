n = int(input())
num = list(map(int, input().split()))

dp = [1] * n
dp[0] = num[0]

for i in range(n):
    for j in range(i):
        if num[j] < num[i]:
            # num 리스트에서 뒤의 인덱스보다 앞의 인덱스가 클 때
            dp[i] = max(dp[i], dp[j] + num[i])
        else:
            dp[i]=max(dp[i], num[i])
# print(dp)
print(max(dp))