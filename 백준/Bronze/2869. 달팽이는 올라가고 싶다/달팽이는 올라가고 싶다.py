a, b, v = map(int, input().split())

res = (v - b) / (a - b)

if res == int(res):
    print(int(res))
else:
    print(int(res) + 1)