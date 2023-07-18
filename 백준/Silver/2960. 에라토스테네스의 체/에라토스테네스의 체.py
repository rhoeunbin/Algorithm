n, k = map(int, input().split())
arr = [False] * (n + 1)
ans = 0

for i in range(2, n + 1):
    if arr[i] == False:
        for j in range(i, n + 1, i):
            if arr[j] == False:
                ans += 1
                if ans == k:
                    print(j)
                    break
            arr[j] = 1
