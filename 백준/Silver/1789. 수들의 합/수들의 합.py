n = int(input())
s = 0
ans = 0
for i in range(1, n + 1):
    s += i
    ans += 1
    if s > n:
        ans -= 1
        break
print(ans)