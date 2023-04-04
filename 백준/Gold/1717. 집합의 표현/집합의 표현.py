import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] * (n + 1)

# 찾기 연산(같은 집합에 속하는지 확인하기 위한 함수)
def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a] 

# 합집합 연산(두 집합을 합치기 위한 함수)
def union(a, b): 
    a = find(a)
    b = find(b) # 대표 노드끼리 연결
    if a != b:
        parent[b] = a

def checkSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(0, n + 1):
    parent[i] = i# 대표 노드를 자기 자신으로 초기화

for _ in range(m):
    que, a, b = map(int, input().split())
    if que == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print("YES")
        else:
            print("NO")