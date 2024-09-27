n = int(input())
d = int(input())
if n < 2:
    print("Before")    
elif n == 2:
    if d == 18: 
        print("Special")
    elif d > 18: 
        print("After")
    else: 
        print("Before")        
else: 
    print("After")