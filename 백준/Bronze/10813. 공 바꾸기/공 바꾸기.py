n, m = map(int, input().split())
# 바구니 n개, m번 공을 바꿈
basket = [ _ for _ in range(1, n + 1)]
for x in range(m):
    i, j = map(int, input().split())
    basket[i - 1], basket[j - 1] = basket[j - 1], basket[i - 1]

print(*basket)