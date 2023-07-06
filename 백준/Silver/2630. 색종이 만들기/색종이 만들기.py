import sys
input = sys.stdin.readline

N = int(input())
paper =[list(map(int,input().split())) for _ in range(N)]
white, blue = 0, 0 # 흰종이,파란종이 개수

def divide(xs,ys,xe,ye): # xs: x시작지점 xe: x끝지점 ys: y시작지점 ye: y끝지점
    global white 
    global blue 
    
    color= paper[xs][ys] 
    case = color
    for x in range(xs,xe):
        for y in range(ys,ye):
            if paper[x][y] != color:
                case = 2
                break

    if case ==2: # 색이 2가지라면 4조각으로 잘라서 함수 실행
        divide((xs+xe)//2,ys,xe,(ys+ye)//2) # 오른쪽 위(1)
        divide(xs,ys,(xs+xe)//2,(ys+ye)//2) # 왼쪽 위(2)
        divide(xs,(ys+ye)//2,(xs+xe)//2,ye) # 왼쪽 아래(3)
        divide((xs+xe)//2,(ys+ye)//2,xe,ye) # 오른쪽 아래(4)
    elif case ==1:
        blue +=1
    elif case ==0:
        white +=1
    return 

divide(0,0,N,N)
print(white)
print(blue)