psg = 0
max_psg = 0

for _ in range(10):
    d, u  = map(int, input().split()) 
    psg += u - d 
    max_psg = max(psg, max_psg) 
    
print(max_psg)