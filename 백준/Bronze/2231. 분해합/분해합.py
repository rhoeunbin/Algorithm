n = int(input())
res = 0

for i in range(1, n + 1):
    num = list(map(int, str(i))) # i의 각 자릿수를 더함
    res = i + sum(num) # 분해합 = 생성자 + i의 각 자리수를 더한 값

    if res == n: # 분해합이 나오면 
        print(i) # 생성자 출력
        break
    
    if i == n: # 생성자 i랑 n이 같으면
        print(0)