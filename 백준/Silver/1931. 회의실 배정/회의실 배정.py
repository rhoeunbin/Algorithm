n = int(input())
h = []

for i in range(n):
    start, end = map(int, input().split())
    h.append((start, end))

h.sort(key= lambda x: (x[1], x[0])) # start, end 

last = 0
cnt = 0

for i, j in h:
    if i >= last:
        cnt += 1
        last = j

print(cnt)