n, m = map(int, input().split())

poketmon = {}
for num in range(1, n + 1):
    name = input().strip()
    poketmon[num] = name
    poketmon[name] = num


for i in range(m):
    f = input().strip()
    if f.isdigit():
        print(poketmon[int(f)])
    else:
        print(poketmon[f])