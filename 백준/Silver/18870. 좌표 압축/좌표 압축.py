import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

lst = list(set(num))
lst.sort()

dic = {lst[i] : i for i in range (len(lst))}
for i in num:
    print(dic[i], end=' ')