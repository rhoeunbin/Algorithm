t = int(input())
for _ in range(t):
    n = int(input())
    zero, one = 0, 1
    for i in range(n):
        zero, one = zero + one, zero
    print(one, zero)