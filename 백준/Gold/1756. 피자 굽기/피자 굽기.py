import sys
input = sys.stdin.readline

D, N = map(int,input().split()) # 오븐의 깊이 D와 피자 반죽의 개수 N
oven = list(map(int,input().split())) # 오븐의 최상단부터 시작하여 깊이에 따른 오븐의 지름이 차례
pizza = list(map(int,input().split())) # 피자 반죽이 완성되는 순서대로, 그 각각의 지름

# [5 6 4 3 6 2 3]
# [5 5 4 3 3 2 2]

for i in range(1, D):
    if oven[i] > oven[i-1]: # 현재>이전 : 현재 = 이전 지름
        oven[i] = oven[i-1]
# print(oven)
cnt = 0

# [2 2 3 3 4 5 5]
for i in reversed(range(D)):  #range(start, stop, step)
    if pizza[cnt] <= oven[i]: # 지름이 반죽보다 작으면 넣을 수 있으므로 cnt +1    
        cnt += 1 

    if cnt == N:
        print(i+1) # cnt랑 반죽 개수 같으면 다 넣은 거니깐 break
        break

else: # 만약 피자가 모두 오븐에 들어가지 않는다면, 0을 출력
    print(0)
