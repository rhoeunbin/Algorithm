n = int(input())

w = []
for i in range(n):
    w.append(input())

w = list(set(w))
w.sort()
w.sort(key=len)

for i in w:
    print(i)