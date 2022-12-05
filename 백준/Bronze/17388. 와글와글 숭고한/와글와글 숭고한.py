s, k, h = map(int,input().split())

if s + k + h < 100 :
    if s < k and s < h :
        print('Soongsil')
    elif k < h and k < s :
        print('Korea')
    else :
        print('Hanyang')
else :
    print('OK')