import sys
input = sys.stdin.readline

m = int(input())
s = set()

for i in range(m):
    c = input().strip().split()
    # print(s)    
    
    if len(c) == 1:
        if c[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
        continue
    # print(s)

    else:
        com, tar = c[0], int(c[1])
        if com == 'add':
            s.add(tar)
        elif com == 'remove':
            s.discard(tar)
        elif com == 'check':
            if tar in s:
                print(1)
            else:
                print(0)
        elif com == 'toggle':
            if tar in s:
                s.discard(tar)
            else:
                s.add(tar)