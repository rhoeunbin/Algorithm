s, k = map(int, input().split())
arr = [1] * k

while sum(arr) < s:
    for i in range(k):
        if sum(arr) < s:
            arr[i] += 1
        else:
            break

res = 1
for n in arr:
    res *= n

print(res)