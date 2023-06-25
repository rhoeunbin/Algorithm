n, k = map(int, input().split())
medal = []
for _ in range(n):
    medal.append(list(map(int, input().split())))

medal.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)

for i in range(n):
    if medal[i][0] == k:
        idx = i

for i in range(n):
    if medal[idx][1:] == medal[i][1:]:
        print(i + 1)
        break