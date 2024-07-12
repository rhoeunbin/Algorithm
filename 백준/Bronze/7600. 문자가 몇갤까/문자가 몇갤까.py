while True:
    sen = input()
    if sen == "#": # "#"이 나오면 입력 멈춤
        break
    alpha = [0] * 26 # 알파벳 리스트
    for i in sen.lower(): # 알파벳을 소문자로 다 바꾸기
        if i.isalpha(): # 만약 알파벳이 있으면
            alpha[ord(i) - 97] = 1 # 1로 바꾸기
        else: # 아니면 넘어감
            continue
    print(alpha.count(1)) # 1의 개수 전부 세기