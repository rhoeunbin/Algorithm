def solution(nums):
    length = len(nums)//2
    
    answer = 0
    monster = {}
    for i in nums:
        if i not in monster:
            monster[i] = 1
        else:
            monster[i] += 1
    
    if len(monster) > length:
        answer = length
    else:
        answer = len(monster)        
    return answer