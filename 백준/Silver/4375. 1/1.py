while True:
    try:
        n = int(input())

    except:
        break
    
    one = 1 # 1로만 이루어진 수
    cnt = 1 # 자릿수

    while True:
        if one % n != 0:
            one = one * 10 + 1
            cnt += 1
        else:
            break
    print(cnt)