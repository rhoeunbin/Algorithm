n = int(input())

oneteam, twoteam, win= 0, 0, 0 

for _ in range(n):
    team, time = input().split()
    m, s = map(int, time.split(':'))
    end = 48 * 60 # 시간 초로 바꿈 => 끝나는 시간
    t = 60 * m + s

    if team == '1':
        if win == 0: # 1팀이 이길 때
            oneteam += end - t
        win += 1
        if win == 0: # 비길 때
            if twoteam > 0:
                twoteam -= end - t
    else: 
        if win == 0: # 2팀이 이길 때
            twoteam += end-t
        win -= 1
        if win == 0: # 비길 때
            if oneteam > 0:
                oneteam -= end - t

# print(oneteam // 60, oneteam % 60)
# print(twoteam // 60, twoteam % 60)
print(str(oneteam // 60).zfill(2), str(oneteam % 60).zfill(2), sep=":")
print(str(twoteam // 60).zfill(2), str(twoteam % 60).zfill(2), sep=":")
