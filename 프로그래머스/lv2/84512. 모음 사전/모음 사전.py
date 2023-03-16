def solution(word):
    answer = 0
    mo = ['A', 'E', 'I', 'O', 'U']
    diff = [781, 156, 31, 6, 1]

    for i in range(len(word)):
        answer += mo.index(word[i]) * diff[i] + 1

    return answer