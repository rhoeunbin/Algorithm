import sys
input = sys.stdin.readline
N, K = map(int, input().split())
 
circle = [i for i in range(1, N+1)]
delete = [] # 제거할 사람 리스트
num = 0 # 제거할 사람 인덱스

while circle:
  num += K-1 # 0부터 시작하니깐
  if num >= len(circle):
    num %= len(circle) 
  delete.append(str(circle.pop(num)))
print(f"<{', '.join(map(str,delete))}>")