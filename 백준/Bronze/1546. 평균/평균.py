n = int(input())
num = list(map(int, input().split()))
max_score = max(num)
plus = sum(num)

print(plus*100 / max_score/ int(n))
