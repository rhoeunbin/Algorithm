n = int(input())
p = []

for i in range(n):
    x, y = map(int, input().split())
    p.append([x,y])
p.sort()
for i in p:
    print(*i)