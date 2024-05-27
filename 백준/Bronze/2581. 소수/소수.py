m = int(input())
n = int(input())
arr = []

for i in range(m, n + 1):
    t = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                t += 1
                break
        if t == 0:
            arr.append(i)

if len(arr) < 1:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))