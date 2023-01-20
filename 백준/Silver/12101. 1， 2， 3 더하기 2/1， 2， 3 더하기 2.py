n,k = map(int,input().split())
num = []
cnt = 0

def dfs(total):
    if total > n:
        return
    if total == n:
        global cnt
        cnt += 1
        if cnt == k:
            print('+'.join(map(str, num)))
        return

    for i in range(1, 4):
        num.append(i)
        dfs(total + i)
        num.pop()

dfs(0)

if cnt < k:
    print(-1)
