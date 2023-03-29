l, p = map(int, input().split())
people = list(map(int, input().split()))
party = l * p
for i in people:
    print(i - party, end=' ')