N = int(input())
cnt = 0
L = len(str(N))

for i in range(L-1):
    cnt += 9 * 10 ** i * (i+1)

print(cnt + (N - 10**(L - 1) + 1) * L)