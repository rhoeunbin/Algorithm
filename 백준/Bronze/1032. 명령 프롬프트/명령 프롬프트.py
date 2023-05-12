t = int(input())
first = list(input())

for _ in range(t - 1):
    dif = list(input().rstrip())
    for i in range(len(first)):
        cmd = []
        if first[i] != dif[i]:
            first[i] = '?'
print(''.join(first))