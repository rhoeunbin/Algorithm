w = list(input())
ans = []
res = []

for i in range(1, len(w) - 1):
    for j in range(i + 1, len(w)):
        a = w[:i]
        b = w[i : j]
        c = w[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        res.append(a + b + c)

for x in res:
    ans.append(''.join(x))

print(sorted(ans)[0])