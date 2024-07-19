n = int(input())
score = list(map(int, input().split()))

ans = 0
cnt = 0
for i in range(n):
    if score[i] == 1:
        cnt += 1
        ans += cnt
    else:
        cnt = 0

print(ans)