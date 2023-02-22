n, t = map(int, input().split())
parent = [i for i in range(n)]

# find : 자신의 값을 최상의 부모의 값으로 초기화
def find(x):
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y

# union : 작은 노드의 값으로 두 노드의 부모를 일치시켜준다. + 부모가 같다면 사이클 발생
def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
        return False
#    elif x > y:
#        parent[x] = y
#        return False
    else:
        parent[x] = y

# 사이클 발생
for i in range(t):
    x, y = map(int, input().split())
    # union가 True : 사이클 발생, 현재 회차(i)를 출력, break

    if find(x) == find(y):
        print(i+1)
        break
    union(x, y)
else:
    print(0)