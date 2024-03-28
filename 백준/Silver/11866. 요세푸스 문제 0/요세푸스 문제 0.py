from collections import deque

n, k = map(int, input().split())
arr = deque([i for i in range(1, n + 1)])
res = []

while len(arr) != 0:
    for i in range(k - 1):
        arr.append(arr.popleft())
    res.append(str(arr.popleft()))

print('<'+', '.join(res)+'>')