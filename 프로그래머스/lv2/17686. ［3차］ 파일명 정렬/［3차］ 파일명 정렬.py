def solution(files):
    answer = []
    for fi in files:
        head, num, tail = '', '',''
        tmp = False

        for i in range(len(fi)):
            if fi[i].isdigit():
                num += fi[i]
                tmp = True
            elif not tmp:
                head += fi[i]
            else:
                tail = fi[i:]
                break
        answer.append((head, num, tail))
    answer.sort(key = lambda x: (x[0].lower(), int(x[1])))
    res = []
    for t in answer:
        res.append(''.join(t))
    return res