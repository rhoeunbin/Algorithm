import sys
input = sys.stdin.readline

n, k = map(int, input().split())
doll = list(map(int, input().split()))

lion = []
for i in range(len(doll)):
    if doll[i] == 1:
        lion.append(i)
        
if len(lion) < k:
    print(-1)
    exit()

start = 0
end = k - 1
ans = sys.maxsize

while True:
    doll = lion[end] - lion[start] + 1
    ans = min(ans, doll)
    if end == len(lion) - 1:
        break
    start += 1
    end += 1
print(ans)

