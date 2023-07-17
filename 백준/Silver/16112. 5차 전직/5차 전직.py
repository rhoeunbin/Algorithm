n, k = map(int, input().split())
exp = list(map(int, input().split()))

exp.sort()

bonus = 0

for i in range(n):
    if i < k:
        bonus += i * exp[i]
    else: 
        bonus += k * exp[i]
print(bonus)