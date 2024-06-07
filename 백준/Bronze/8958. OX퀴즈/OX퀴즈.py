t = int(input())

for _ in range(t):
    res = list(input())
    score = 0
    ans = 0

    for i in res:
        if i == 'O':
            score += 1
        else:
            score = 0
        ans += score

    print(ans)