import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = 100 - n
b = 100 - m
c = 100 - (a + b)
d = a * b

e = d // 100
f = d % 100

print(a, b, c, d, e, f)
print(c + e, f)