n = int(input())
plan = list(map(int, input().split()))
time = sum(plan) + (8 * (n - 1))

w, t = time // 24, time % 24

print(w, t)