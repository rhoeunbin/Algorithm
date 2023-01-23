import sys
input = sys.stdin.readline

N = int(input())
recommend = int(input())
student = list(map(int,input().split()))
cand = {}

for s in student:
    if s not in cand.keys():
        if len(cand.keys()) == N:
            min_val = 1000
            min_key = 1
            for key, value in cand.items():
                if value < min_val:
                    min_key = key
                    min_val = value
            cand.pop(min_key)
        cand[s] = 0
    else:
        cand[s] += 1
        
print(*sorted(cand.keys()))