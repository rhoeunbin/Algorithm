import sys
input = sys.stdin.readline

num = int(input())

p = []
m = []
one = []

for i in range(num):
    n = int(input())
    if n > 1:
        p.append(n)
    elif n <= 0:
        m.append(n)
    else:
        one.append(n)

p.sort()
m.sort(reverse=True)
# print(p)
# print(m)

ans = 0

while p:
    a = p.pop()
    if p:
        b = p.pop()
        ans += a * b
    else:
        ans += a

while m:
    a = m.pop()
    if m:
        b = m.pop()
        ans += a * b
    else:
        ans += a

ans += sum(one)
print(ans)