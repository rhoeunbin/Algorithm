n, m, k = map(int,input().split())
min_ans = max(n - (m * k), 0)
max_ans = n - m*(k - 1) - 1

print(min_ans, max_ans)