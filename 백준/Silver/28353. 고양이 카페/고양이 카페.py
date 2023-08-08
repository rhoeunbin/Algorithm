import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cat = list(map(int, input().split()))
cat.sort()
# print(cat)
ans = 0
start = 0
end = n - 1

while start < end:
    if cat[start] + cat[end] <= k:
        # print(cat[start],cat[end])
        start += 1
        end -= 1
        ans += 1
    else:
        # print(cat[start],cat[end])
        end -= 1

print(ans)