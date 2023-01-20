n, k = map(int, input().split())

num = []
ans = set()

def dfs(num, answer):
    if num == n:
        ans.add(tuple(answer))
        return

    if num + 1 <= n:
        dfs(num + 1, answer + [1])

    if num + 2 <= n:
        dfs(num + 2, answer + [2])

    if num + 3 <= n:
        dfs(num + 3, answer + [3])

dfs(0, [])

if len(ans) < k: 
    print(-1)
else:
    ans = list(ans)
    ans.sort()
    answer = ans[k-1]
    print(*answer, sep="+")