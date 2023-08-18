s = input()

s_list = []

for _ in s:
    s_list.append(s)
    s = s[1:]

for i in sorted(s_list):
    print(i)