n, m = map(int,input().split())
ans = []

def back(s):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(s, n + 1):
        if i not in ans:
            ans.append(i)
            back(i)
            ans.pop()

back(1)