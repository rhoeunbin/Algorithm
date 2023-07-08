n, k = map(int,input().split()) # n: 동전개수, k: 목표금액
coin = [0] * n

for i in range(n):
    coin[i] = int(input())

cnt = 0 # 동전 수

for i in range(n - 1, -1, -1): # n - 1 ~ 0 역순으로 반복
    if coin[i] <= k: # k 보다 동전 가치가 작거나 같으면
        cnt += int(k / coin[i])
        k = k % coin[i]

print(cnt)
