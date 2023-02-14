# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
  # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 우너소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드, 간선(union 연산) 개수 input
n, m = map(int, input().split())
gen = list(input().split()) # 남초 대학교라면 M, 여초 대학교라면 W
parent = [0] * (n + 1)

edges = [] # 모든 간선을 담을 리스트
result = 0 # 최종 비용 담을 변수
cnt = 0 # 경로의 수

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# 모든 간선에 대한 정보 입력 받기
for i in range(m):
    u, v, d = map(int, input().split())
    # 비용순으로 정렬하기 위해 튜플의 첫번째 원소를 비용으로 설정
    edges.append((d, u, v))

# 간선을 비용순으로 정렬
edges.sort() 

# 간선을 하났기 확인
for edge in edges:
    d, u, v = edge

    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, u) != find_parent(parent, v) and gen[u-1] != gen[v-1]:
        union_parent(parent, u, v)
        result += d
        cnt += 1
    if cnt == n - 1: # n - 1일 때 경로가 있는 것
        break
if cnt != n - 1: # 모든 학교를 연결하는 경로가 없을 경우
    result = -1

print(result)