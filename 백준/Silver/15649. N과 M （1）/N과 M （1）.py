import sys
input = sys.stdin.readline
from itertools import permutations #순열 함수 사용

n, m = map(int,input().split())
arr = list(range(1,n+1)) 
answer = list(permutations(arr,m))
for i in answer:
    print(*i)