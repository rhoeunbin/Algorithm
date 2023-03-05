import sys
input = sys.stdin.readline

n, k = map(int,input().split())
suyeol = list(map(int, input().split()))

result = []
result.append(sum(suyeol[:k]))

for i in range(n - k):
    result.append(result[i] - suyeol[i] + suyeol[k+i])

print(max(result))