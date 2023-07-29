n, m = map(int, input().split())
idol = {}
for _ in range(n):
    team = input()
    mem = [input() for _ in range(int(input()))]
    # mem = []
    # for _ in range(int(input())):
    #     mem.append(input())
    mem.sort()
    idol[team] = mem

for _  in range(m):
    name = input()
    quiz = int(input())
    if quiz == 1:
        for t, m in idol.items():
            if name in m:
                print(t)
    else:
        for i in idol[name]:
            print(i)
