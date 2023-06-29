n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

l = a + b
l.sort()
print(*l)