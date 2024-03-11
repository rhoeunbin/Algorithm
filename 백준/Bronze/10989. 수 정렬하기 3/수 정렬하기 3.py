import sys
input = sys.stdin.readline

n = int(input())

# 각 수의 등장 횟수를 저장하기 위한 리스트 생성
arr = [0] * 10001

# n개의 수를 입력 받아 등장 횟수를 증가시킴
for _ in range(n):
    num = int(input())
    arr[num] += 1

# 리스트를 순회하면서 등장 횟수가 0이 아닌 수를 출력
for i in range(10001):
    if arr[i]:
        for j in range(arr[i]):
            print(i)