import sys
input = sys.stdin.readline

guitar = []
n = int(input())
for _ in range(n):
    s = input().rstrip()
    
    res = 0 # 자릿수합
    for i in s:
        if i.isdigit():
            res += int(i)
    guitar.append((s, res))
    
guitar.sort(key=lambda x:(len(x[0]), x[1], x[0]))

for i in guitar:
    print(i[0])