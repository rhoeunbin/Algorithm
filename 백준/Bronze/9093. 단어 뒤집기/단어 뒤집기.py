import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    sen = list(input().split())

    for w in sen:
        print(w[::-1], end=" ")
    print()