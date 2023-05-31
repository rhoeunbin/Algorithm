n = int(input())
arr = [0] * n
stack = []

for i in range(n):
    arr[i] = int(input())

num, res = 1, True
ans = ''

for i in range(n):
    if arr[i] >= num: # 현재수열값 >= 오름차순 자연수 값이 같아질 때
        while arr[i] >= num:
            stack.append(num)
            num += 1
            ans += '+\n'
        stack.pop()
        ans += '-\n'
    else: # # 현재수열값 < 오름차순 자연수
        n = stack.pop()

        if n > arr[i]: # 스택의 가장 위의 수가 만들어야 하는 수열의 수보다 크면 수열 출력 X
            print('NO')
            res = False
            break
        else:
            ans += '-\n'

if res:
    print(ans)