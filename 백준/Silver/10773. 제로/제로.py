k = int(input())
num = []
for _ in range(k):
    n = int(input())
    if n != 0:
        num.append(n)
    else:
        num.pop()
print(sum(num))