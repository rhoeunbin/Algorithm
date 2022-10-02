import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int,input().split())
    cnt= 0

    for i in range(a, b+1): #a부터 b값 전체를 세기 때문에 
        cnt += str(i).count('0') #숫자를 문자열로 바꾸어 count하면 됨
    
    print(cnt)