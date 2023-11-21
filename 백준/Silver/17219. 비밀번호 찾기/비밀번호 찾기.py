n, m = map(int, input().split())
ans = {}

for i in range(n):
    site, pw = input().split()
    ans[site] = pw

for i in range(m):
    print(ans[input().strip()])