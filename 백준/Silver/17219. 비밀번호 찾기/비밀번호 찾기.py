n, m = map(int,input().split())
pw = {}

for _ in range(n):
    site, name = input().split()
    pw[site] = name

for _ in range(m):
    print(pw[input().strip()])