t = int(input())
for _ in range(t):
    n = int(input())
    zero, one = 1, 0 # zero: 0개수, one: 1개수
    for i in range(n):
        zero, one = one, zero + one # zero와 one에 대해 피보나치적용
    print(zero, one)

'''
0이 출력되는 획수의 규칙 1 // 0 1 1 2 3
1이 출력되는 획수의 규칙 0 1 1 2 3 이후로 같음
=>  zero, one = one, zero + one'''