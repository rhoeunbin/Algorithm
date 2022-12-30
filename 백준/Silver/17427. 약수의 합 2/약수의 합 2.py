n = int(input())

gN = 0
for i in range(1, n+1):
    gN += (n//i)*i

print(gN)