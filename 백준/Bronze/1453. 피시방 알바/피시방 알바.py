import sys

input = sys.stdin.readline

n = int(input())
seat = list(map(int, input().split()))
s = len(list(set(seat)))
print(n-s)