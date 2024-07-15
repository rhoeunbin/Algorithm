n = int(input())
f = n % 8 # 8을 주기로 반복
'''
  1  2  3  4  
              5
    8  7  6
  9            
    10  11  12 
              13 
    16  15  14 
'''

if f == 1:
    print(1)
elif f == 2 or f == 0:
    print(2)
elif f == 3 or f == 7:
    print(3)
elif f == 4 or f == 6:
    print(4)
elif f == 5:
    print(5)