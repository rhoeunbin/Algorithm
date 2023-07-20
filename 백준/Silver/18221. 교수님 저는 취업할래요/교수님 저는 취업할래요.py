n = int(input())
seat = []

for i in range(n):
    s = list(map(int, input().split()))
    for j in range(n):
        if s[j] == 2:
            sung = (i, j)
        elif s[j] == 5:
            pro = (i, j)
    seat.append(s)

dis = ((sung[0] - pro[0]) ** 2 + (sung[1] - pro[1]) ** 2) # 성규랑 교수 사이의 거리

if dis >= 25: # 거리가 5이상이면
    cnt = 0 # 성규랑 교수님 사이에 있는 행과 열 카운트
    for i in range(min(sung[0], pro[0]), max(sung[0], pro[0]) + 1):
        for j in range(min(sung[1], pro[1]), max(sung[1], pro[1]) + 1):
            if seat[i][j] == 1:
                cnt += 1
                '''교수의 위치가 (a,b), 성규의 위치가 (c,d)라고 하면 반복문의 수도코드는 다음과 같다. arr은 입력받은 배열이다.
                (a-c)**2 + (b-d)**2 >= 25

                for i가 (min(a, c)부터 max(a, c)까지):
                for j가 (min(b, d)부터 max(m, d)까지):
                    arr[i][j]가 1이라면 학생이므로 카운팅'''
                
    if cnt >= 3: # 만날 수 있음
        print('1')
    else:
        print("0")
else:
    print("0")