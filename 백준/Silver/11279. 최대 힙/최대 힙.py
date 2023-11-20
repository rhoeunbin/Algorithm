import heapq
import sys
input = sys.stdin.readline

heap = []

for i in range(int(input())):
    num = int(input())

    if num != 0:
        heapq.heappush(heap, -num)
    else:
        if not heap:
            print(0)
        else:
            print(-(heapq.heappop(heap)))