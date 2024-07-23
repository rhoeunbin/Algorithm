n, m = map(int, input().split())
listen = set()
watch = set()
ans =[]

for _ in range(n):
    listen.add(input())
for _ in range(m):
    watch.add(input())

for i in listen:
    if i in watch:
        ans.append(i)
ans.sort()
print(len(ans))

for i in ans :
    print(i)