n = int(input())

friend = [list(input()) for _ in range(n)]
graph = [[0 for _ in range(n)] for _ in range(n)]
# [[0] * n for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if friend[i][j] == 'Y' or (friend[i][k] == 'Y' and friend[k][j] == 'Y'):
                graph[i][j] = 1

answer = 0 
for row in graph:
    answer = max(answer, sum(row))
print(answer)