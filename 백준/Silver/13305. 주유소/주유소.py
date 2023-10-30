n = int(input())
city = list(map(int, input().split()))
L = list(map(int, input().split()))

minL = L[0]
ans = 0
for i in range(len(city)):
    if minL > L[i]:
        minL = L[i]
    ans += minL * city[i]
print(ans)