n = int(input())
graph = []
for i in range(n):
    t, s = map(int, input().split())
    graph.append((t, s))
    # Ti 시간이 걸리고 Si 시 내에 이 일을 처리하여야 한다

graph.sort(key = lambda x: x[1], reverse=True)

ans = graph[0][1] - graph[0][0]

for i in range(1, n):
    if ans > graph[i][1]:
        ans = graph[i][1] - graph[i][0]

    else:
        ans -= graph[i][0]

        
if ans > 0:
    print(ans)
else:
    print(-1)