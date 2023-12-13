for _ in range(3):
    hs, ms, ss, he, me, se = map(int, input().split())
    t1 = hs*60*60 + ms*60 + ss
    t2 = he*60*60 + me*60 + se
    t = t2 - t1
    h = t//60//60 % 24
    m = t//60 % 60
    s = t % 60
    print(h, m, s)