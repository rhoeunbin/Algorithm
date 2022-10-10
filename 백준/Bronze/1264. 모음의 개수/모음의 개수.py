import sys
input = sys.stdin.readline

vowels = ['a','e','i','o','u'] #모음 리스트 만들기

while True:
    stc = list(input().lower())
    cnt = 0

    if stc[0] == '#':
        break

    for j in stc:
        if j in vowels:
            cnt += 1
    
    print(cnt)