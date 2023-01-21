n = int(input())
people = list(map(int, input().split()))

'''
0 0 1 0 왼쪽에 두명이 있으므로 2칸을 비워두고 자리를 채운다.
0 2 1 0 
0 2 1 3
4 2 1 3
'''
ans = [0] * n

for i in range(n):
    cnt = 0 # 자신의 왼쪽에 있는 키 큰 사람 수
    for j in range(n):
        if cnt == people[i] and ans[j] == 0: # 키 큰 사람의 수가 맞고 그 자리에 아무도 없다
            ans[j] = i + 1
            # print('c1')
            # print(ans)
            break

        elif ans[j] == 0: # 자리에 아무도 없으면 왼쪽 키 큰 사람 수 count
            cnt += 1
        # print('c2')
        # print(ans)

print(*ans)