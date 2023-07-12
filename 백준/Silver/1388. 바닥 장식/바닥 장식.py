n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

# 두 개의 ‘-’가 인접해 있고, 같은 행
cnt = 0
for i in range(n):
    o = ''
    for j in range(m):
        if graph[i][j] == '-':
            if graph[i][j] != o:
                cnt += 1
        o = graph[i][j]

#  두 개의 ‘|’가 인접해 있고, 같은 열
for j in range(m):
    o = ''
    for i in range(n):
        if graph[i][j] == '|':
            if graph[i][j] != o:
                cnt += 1
        o = graph[i][j]

print(cnt)