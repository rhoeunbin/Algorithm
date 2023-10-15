n = int(input())
ans_f = 0
ans_s = 0
ans_t = 0
for i in range(1, n + 1):
    ans_f += i
    ans_t += i*i*i
print(ans_f)
print((ans_f)*(ans_f))
print(ans_t)