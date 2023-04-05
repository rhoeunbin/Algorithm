import sys
sys.setrecursionlimit(10 * 7)
input = sys.stdin.readline

n, m, k = map(int, input().split())
friend = [0] + list(map(int,input().split()))
parent = [i for i in range(n+1)]

# 찾기
def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a] 

# 합집합
def union(a, b): 
    a = find(a)
    b = find(b) # 대표 노드끼리 연결
    if a != b:
        if friend[a] < friend[b]:
            parent[b] = a
        else:
            parent[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

ans = 0

for i in range(1, n + 1):
    if parent[i] == i:
        ans += friend[i]

if ans > k:
    print('Oh no')
else:
    print(ans)