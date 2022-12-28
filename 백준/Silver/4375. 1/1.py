while True:
    try:
        n = int(input())
    except:
        break
    cnt = 1 # num의 자리수 체크
    num = 0

    while True:
        num = num *10 + 1 # num에 나머지를 저장 모든 자리수가 1인 수 만듦
        ''' num = 0
            num = 0 * 10 +1 >> num은 1
            num = 1 * 10 +1 >> num은 11
            num = 11 * 10 +1 >> num은 111'''
        num %= n
        ''' 11 % 3 = (1 * 10 + 1) % 3 = 2
            111 % 3 = (11 * 10 + 1) % 3 = 0
        '''
        if num == 0:
            print(cnt)
            break
        cnt += 1