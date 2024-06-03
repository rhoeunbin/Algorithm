word = input().upper()
set_word = list(set(word))
cnt = []

for i in set_word:
    word_count = word.count
    cnt.append(word_count(i))

if cnt.count(max(cnt)) > 1:
    print('?')

else:
    print(set_word[(cnt.index(max(cnt)))])