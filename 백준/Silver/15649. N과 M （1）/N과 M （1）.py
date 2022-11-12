# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성
from itertools import permutations #순열 라이브러리 사용
n, m = map(int,input().split())
arr = list(range(1, n+1)) # n개의 리스트 만들기
answer = list(permutations(arr, m)) # arr에서 원소 개수가 m인 순열 뽑기
for per in answer:
    print(*per) # 튜플 형태를 없애기 위해 *사용