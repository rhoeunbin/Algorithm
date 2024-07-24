t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    prior = list(map(int, input().split()))

    res = 1

    while prior:
        if prior[0] < max(prior):
            prior.append(prior.pop(0))
        else:
            if m == 0:
                break
            prior.pop(0)
            res += 1

        if m > 0:
            m -= 1
        else:
            m = len(prior) - 1

    print(res)            
