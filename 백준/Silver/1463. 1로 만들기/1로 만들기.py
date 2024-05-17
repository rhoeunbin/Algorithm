n = int(input())
dp = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1 # 2와 3으로 나누어 떨어지지 않으면 어차피 1을 빼기 때문에

    # 여기서 if elif else를 사용하면 안된다. if만 이용해야 세 연산을 다 거칠 수 있다.
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
        # 1을 더하는 것은 dp는 결과가 아닌 계산한 횟수를 저장하는 것 이기 때문이다. 
        # dp[i]에는 더하지 않는 이유는 이미 1을 뺄 때 1을 더해준 이력이 있기 때문
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[n])