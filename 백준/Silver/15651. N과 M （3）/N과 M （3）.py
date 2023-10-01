n, m = map(int, input().split())
su = []

def back():
    if len(su) == m:
        print(' '.join(map(str, su)))
        return
    for i in range(1, n + 1):
        su.append(i)
        back()
        su.pop()
back()
