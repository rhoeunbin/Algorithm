n = int(input())
num = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    for j in range(i):
        if num[i] > num[j] and dp[i] < dp[j]:
            # num 리스트에서 뒤의 인덱스보다 앞의 인덱스가 크고 dp에서 뒤 인덱스가 앞의 인덱스보다 클 때
            dp[i] = dp[j] # 앞뒤의 값을 같게 만들어주고
    dp[i] += 1 # +1을 함
print(max(dp))