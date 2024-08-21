idx = 1
while True:
    sen = input()
    if sen == "Was it a cat I saw?":
        break
    print(sen[::idx + 1])
    idx += 1