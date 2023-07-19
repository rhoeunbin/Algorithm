n = int(input())
pat = input().split('*')

for i in range(n):
    name = input()
    if len(pat[0]) + len(pat[1]) > len(name):
        print("NE")
    # if pat[0] == name[0] and pat[-1] == name[-1]:
    elif pat[0] == name[:len(pat[0])] and pat[1] == name[-len(pat[1]):]:
        print('DA')
    else:
        print('NE')