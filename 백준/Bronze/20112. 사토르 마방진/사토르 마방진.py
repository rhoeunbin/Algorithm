n = int(input())
arr = []
for i in range(n):
    s = input()
    arr.append(s)

sator = "YES"
for i in range(n):
    row = ""
    col = ""
    row = arr[i]
    for j in range(n):
        col += arr[j][i]

    if row != col:
        sator = "NO"

print(sator)