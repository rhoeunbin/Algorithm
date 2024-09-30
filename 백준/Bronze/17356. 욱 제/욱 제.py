a, b = map(float, input().split())
m = (b - a)/400
res = 1 / (1 + 10**m)
print(res)
