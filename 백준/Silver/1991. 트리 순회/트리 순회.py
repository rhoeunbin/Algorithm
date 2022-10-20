import sys
input = sys.stdin.readline

n = int(input()) #이진 노드 트리의 개수
tree = {}
# 전위 순회 : 현재 -> 왼쪽 -> 오른쪽 노드 ABDCEFG
# 중위 순회 : 왼쪽 -> 현재 -> 오른쪽 노드 DBAECFG
# 후위 순회 : 왼쪽 -> 오른쪽 -> 현재 노드 DBECFGA

for i in range(n):
    root, left, right = input().split()
    tree[root] = [left, right] # tree 딕셔너리에 저장

# 전위 순회
def pre_order(now):
    if now =='.':
        return # 자식 노드가 없을 때
    print(now, end='') # 현재 노드
    pre_order(tree[now][0]) # 왼쪽 자식 노드 탐색
    pre_order(tree[now][1]) # 오른쪽 자식 노드 탐색

# 중위 순회
def in_order(now):
    if now =='.':
        return
    in_order(tree[now][0])
    print(now, end='')
    in_order(tree[now][1])

# 후위 순회
def post_order(now):
    if now =='.':
        return
    post_order(tree[now][0])
    post_order(tree[now][1])
    print(now, end='')

pre_order('A')
print()
in_order('A')
print()
post_order('A')
