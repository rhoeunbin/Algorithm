x = int(input())
line = 1

while x > line:
    x -= line # x가 몇번째에 위치하는지 알 수 있음
    line += 1

if line % 2 == 0: # 짝수 => 분모 -1 분자 +1
    up = x
    down = line - x + 1

else: # 홀수 => 분모 +1 분자 -1
    up = line - x + 1
    down = x

print(up, '/', down, sep="")