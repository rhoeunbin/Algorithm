n, m = map(int, input().split())
ans = []

def back(s):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(s, n + 1):
        ans.append(i) # 배열 추가
        back(i) # 재귀
        ans.pop()
back(1)