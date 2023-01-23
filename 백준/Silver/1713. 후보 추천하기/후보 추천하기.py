N = int(input()) # 사진틀의 개수
recommend = int(input()) # 전체 학생의 총 추천 횟수
student = list(map(int, input().split())) # 추천받은 학생

pic = [] # 사진틀
cnt = [] # 추천 수 저장 리스트

for i in range(recommend):
    if student[i] in pic:
        for j in range(len(pic)):
            if student[i] == pic[j]:
                cnt[j] += 1 #점수증가
    else: # 사진틀에 없고
        if len(pic) >= N: # 사진틀 가득 참
            for j in range(N):
                if cnt[j] == min(cnt): #가장 작은 점수 찾기
                    del pic[j]
                    del cnt[j]
                    break #먼저 찾으면 (오래된거일수록 인덱스 앞에 있음)
        pic.append(student[i]) #새로운 거 뒤에 더해줌
        cnt.append(1)

pic.sort()
print(' '.join(map(str, pic)))