n = list(input())
ans = 0

for i in range(len(n)):
    n.insert(0, n[-1])
    del n[-1]
    ans += int("".join(n))
print(ans)
