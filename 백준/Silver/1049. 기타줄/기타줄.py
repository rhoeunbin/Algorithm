n, m = map(int, input().split())
pac = []
co = []
for i in range(m):
    p, c = map(int, input().split())
    pac.append(p)
    co.append(c)

pac_min = min(pac)
ans = 0
while n > 0:
    if n >= 6:
        co_min = min(co) * 6
        n -= 6
    else:
        co_min = min(co) * n
        n -= n
    if co_min < pac_min:
        ans += co_min
    else:
        ans += pac_min
print(ans)