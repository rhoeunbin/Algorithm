while True:
    pw = input()
    if pw == "END":
        break
    else:
        pw = pw[::-1]
        print(pw)