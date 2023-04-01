import sys
input = sys.stdin.readline

n, m = map(int,input().split())
correct = set([input() for _ in range(n)])  
cnt = 0

for i in range(m):
    word = input()
    if word in correct:
        cnt += 1
print(cnt)
