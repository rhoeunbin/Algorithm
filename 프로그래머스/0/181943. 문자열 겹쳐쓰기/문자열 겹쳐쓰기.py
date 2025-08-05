def solution(mys, overs, s):
    answer = mys[:s] + overs + mys[len(overs) + s:]
    
    return answer