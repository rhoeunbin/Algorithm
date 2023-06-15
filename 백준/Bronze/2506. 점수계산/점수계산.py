n = int(input())
s = list(map(int, input().split()))
cnt = 0
ans = 0

for i in range(n):
    if s[i] == 1:
        cnt += 1
        ans += cnt
    else:
        cnt = 0
print(ans)