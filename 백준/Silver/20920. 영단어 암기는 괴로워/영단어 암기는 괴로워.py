import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
word = {} 

for _ in range(n):
    w = input().rstrip()
    
    if len(w) >= m: 
        if w in word: 
            word[w] += 1
        else: 
            word[w] = 1

word = sorted(word.items(), key = lambda x : (-x[1], -len(x[0]), x[0])) # x[0] = 단어, x[1] = 단어 빈도수
# -x[1] = 자주 나오는 단어 앞에 배치
# -len(x[0]) = 단어 길이 길수록 앞에 배치
# x[0] = 단어 사전 순 정렬

for i in word:
    print(i[0])