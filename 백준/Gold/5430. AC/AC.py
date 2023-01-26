from collections import deque

T = int(input())
for _ in range(T):
    func = input()
    k = int(input())
    # q: 입력받은 배열 양방향 큐에 담기
    queue = deque(input()[1:-1].split(','))
    # flag: R(뒤집기)를 한 번만 실행하기 위함
    cnt = 0
    
    if k == 0:  
        queue = []
    
    for c in func:
        if c == 'R':
            cnt += 1
        elif c == 'D':
            if len(queue) == 0:
                print('error')
                break
            else:
                if cnt % 2 == 1:
                    queue.pop()
                else:
                    queue.popleft()
                        
    else:
        if cnt % 2 == 0:
            # print(queue)
            print('[' + ','.join(queue) + ']')
        else:
            queue.reverse()
            # print('1',queue)
            print('[' + ','.join(queue) + ']')