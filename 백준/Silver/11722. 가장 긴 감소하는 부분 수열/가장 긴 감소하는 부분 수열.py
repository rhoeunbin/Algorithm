n = int(input())
num = list(map(int, input().split()))

dp = [1] * n
for i in range(n):
    for j in range(i):
        if num[j] > num[i]:
            # num 리스트에서 뒤의 인덱스보다 앞의 인덱스가 작을 때
            dp[i] = max(dp[i], dp[j]+1)
# print(dp)
print(max(dp))