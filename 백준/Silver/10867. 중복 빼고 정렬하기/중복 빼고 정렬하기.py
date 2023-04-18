n = int(input())
num = set(list(map(int,input().split())))
set_num = sorted(set(num))

for i in set_num:
    print(i, end = ' ')