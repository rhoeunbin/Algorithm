def round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)
    

n = int(input())

if n: # 의견이 있다면
    o = sorted([int(input()) for _ in range(n)])
    exc = round(n * 0.15)
    score = o[exc:n - exc]
    print(round(sum(score) / len(score)))  
else: # 의견이 없으면
    print(0)