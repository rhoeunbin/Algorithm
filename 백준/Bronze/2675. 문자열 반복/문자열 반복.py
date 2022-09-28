t = int(input())

for tc in range(t):
    n , w = input().split()
    word = ''

    for tc in w:
        word += int(n)*tc
    print(word)