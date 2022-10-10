import sys
input = sys.stdin.readline

while True:
    sen = input().rstrip().upper()
    if sen == "#":
        break
    cnt = 0
    for i in sen:
        if i in 'AEIOU':
            cnt += 1
    print(cnt)
