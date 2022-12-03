def solution(survey, choices):
    answer = ''
    kmbti = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i in range(len(survey)):
        if choices[i] < 4: # 4보다 점수가 낮으면
            kmbti[survey[i][0]] += 4 - choices[i] # 첫 번째 캐릭터는 i+1번 질문의 비동의
        else:
            kmbti[survey[i][1]] += abs(4 - choices[i]) # 동의

    if kmbti['R'] >= kmbti['T']: # 각 성격 유형 점수가 같으면, 두 성격 유형 중 사전 순
        answer += 'R'
    else:
        answer += 'T'

    if kmbti['C'] >= kmbti['F']:
        answer += 'C'
    else:
        answer += 'F'

    if kmbti['J'] >= kmbti['M']:
        answer += 'J'
    else:
        answer += 'M'

    if kmbti['A'] >= kmbti['N']:
        answer += 'A'
    else:
        answer += 'N'
        
    return answer