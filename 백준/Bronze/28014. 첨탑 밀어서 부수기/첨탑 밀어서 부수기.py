n = int(input())
h = list(map(int, input().split()))
cnt = 1

for i in range(1, n):
    if h[i] >= h[i - 1]:
        cnt += 1
    else:
        continue
print(cnt)
