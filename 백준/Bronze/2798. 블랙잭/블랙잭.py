n, m = map(int,input().split())
num = list(map(int,input().split()))

ans = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            hop = num[i] + num[j] + num[k]
            if hop > m:
                continue
            else:
                ans = max(ans, hop)

print(ans)