import sys
import heapq
input = sys.stdin.readline

n =int(input())  #연산의 개수
heap = []        #heap 생성

for i in range(n):         #n만큼
    num = int(input())  #num = [1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0]
    if num != 0:       
        heapq.heappush(heap, (abs(num), num))  
    else :
        if heap:   
            print(heapq.heappop(heap)[1])
        else:
            print(0)
