import sys
input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    cal = list(input().split())
    if cal[0] == 'add':
        s.add(int(cal[1]))
    elif cal[0] == 'check':
        if int(cal[1]) in s:
            print(1)
        else:
            print(0)
    elif cal[0] == 'remove':
        try:
            s.remove(int(cal[1]))
        except:
            pass
    elif cal[0] == 'toggle':
        if int(cal[1]) in s:
            s.remove(int(cal[1]))
        else:
            s.add(int(cal[1]))
    elif cal[0] == 'all':
        s = set([i for i in range(1,21)])
    else:
        s = set()