for i in range(int(input())):
    H, W, N = map(int, input().split( )) # H = 각 호텔의 층 수, W = 각 층의 방 수, N= 몇 번째 손님

    floor = N % H 
    room_line = (N // H) + 1
    if floor == 0: # 나머지가 0으로 나눠 떨어질때를 고려
        floor = H
        room_line -= 1
    
    print(floor * 100 + room_line)