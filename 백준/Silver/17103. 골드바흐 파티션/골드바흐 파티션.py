import sys
input = sys.stdin.readline

t = int(input())
gold = []

for i in range(t):
    n = int(input())
    gold.append(n)
# print(gold)
m = max(gold)

prime = [False, False] + [True] * (m-1)

for i in range(2, int(m**0.5) + 1):
    if prime[i]:
        for j in range(2 * i, m + 1, i):
            prime[j] = False    

for num in gold:
    cnt = 0
    for i in range((num//2) + 1):
        if prime[i] and prime[num - i]:
            cnt += 1
    print(cnt)