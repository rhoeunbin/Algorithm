import sys
from itertools import permutations

n = int(input())
k = int(input())

# 12 112 11 212 21 121 122
card = [int(input()) for _ in range(n)]
res = set()

for i in list(permutations(card, k)):
    res.add(''.join(list(map(str, i))))

print(len(res))