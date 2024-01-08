n = int(input())
p = int(input())

ans = 0

if n >= 5:
    ans = max(ans, 500)
if n >= 10:
    ans = max(ans, p//10)
if n >= 15:
    ans = max(ans, 2000)
if n >= 20:
    ans = max(ans, p//4)

if p <= ans:
    print(0)
else:
    print(p - ans)