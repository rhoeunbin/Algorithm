a = int(input()) # 원래 고기의 온도
b = int(input()) # 목표 온도
c = int(input()) # 얼어있는 고기를 1도 데우는 데 걸리는 시간
d = int(input()) # 얼어있는 고기를 해동하는 데 걸리는 시간
e = int(input()) # 얼어 있지 않은 고기를 1도 데우는 데 걸리는 시간

if a < 0:
    ans = (- a * c) + d + (b * e)
else:
    ans = (b - a) * e

print(ans)