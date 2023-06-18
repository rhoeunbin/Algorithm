def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

N = int(input())
switch = [0] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    g, c = map(int, input().split())

    if g == 1:
        for i in range(c, N + 1, c):
            change(i)
    else:
        change(c)
        for j in range(N // 2):
            if c + j > N or c - j < 1 : break
            if switch[c + j] == switch[c - j]:
                change(c + j)
                change(c - j)
            else:
                break
                
for i in range(1, N + 1):
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()