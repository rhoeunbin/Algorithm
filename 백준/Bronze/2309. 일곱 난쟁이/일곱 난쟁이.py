nan = []

for _ in range(9):
    nan.append(int(input()))
nan.sort()
nansum = sum(nan)

for i in range(len(nan)):
    for j in range(i + 1, len(nan)):
        if nansum - nan[i] - nan[j] == 100:
            for k in range(len(nan)):
                if k == i or k == j:
                    pass
                else:
                    print(nan[k])
            exit()