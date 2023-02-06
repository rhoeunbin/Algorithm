n = int(input())
s = [int(input()) for _ in range(n)] # 계단 리스트
dp = [0] * n # dp 리스트

if len(s) <= 2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(s))
else: # 계단이 3개 이상일 때
    dp[0] = s[0] # 첫째 계단 수동 계산
    dp[1] = s[0] + s[1] # 둘째 계단까지 수동 계산
    for i in range(2, n): # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
        dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])
        # dp[3] = dp[0] + s[2] + s[3] 혹은 dp[1] + s[3] 
    # print([dp]) [[10, 30, 35, 55, 65, 75]]
    print(dp[-1])