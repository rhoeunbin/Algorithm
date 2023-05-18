n, m = map(int, input().split())
# 바구니를 총 N개, M번 바구니의 순서를 역순
basket = [i for i in range(1, (n + 1))]
for i in range(m):
    i, j = map(int, input().split())
    temp = basket[i - 1 : j]
    temp.reverse()
    basket[i - 1 : j] = temp
print(*basket)