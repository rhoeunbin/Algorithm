import sys
sys.setrecursionlimit(111111)

def dfs(v):
    global result
    visited[v] = True
    team.append(v)
    next = num[v] # 다음 방문 장소

    if visited[next]: #방문가능한 곳이 끝났는지
        if next in team: #사이클 가능 여부
            result += team[team.index(next):] #사이클 되는 구간 부터만 팀을 이룸
        return
    else: # 방문 안 하면 재귀
        dfs(next)

t = int(input())
for _ in range(t):
    n = int(input())
    num = [0] + list(map(int, input().split()))

    visited = [False] * (n + 1)
    result = [] # 팀에 속한 사람

    for i in range(1, n + 1):
        if not visited[i]:
            team = []
            dfs(i)
    print(n - len(result))