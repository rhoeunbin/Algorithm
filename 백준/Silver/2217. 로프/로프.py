n = int(input())
l = []

for i in range(n):
    l.append(int(input()))

l.sort(reverse=True)
res = []

for j in range(n):
    res.append(l[j] * (j + 1))

print(max(res))