import sys
input = sys.stdin.readline

n, m = map(int, input().split())

poketmon = {}
for i in range(1, n + 1):
    name = input().strip()
    poketmon[i] = name
    poketmon[name] = i

for _ in range(m):
    com = input().strip()

    if com.isdigit():  # int 이면
        print(poketmon[int(com)])
    else:
        print(poketmon[com])