def check_w(s: str):
    offset = int(1)
    start = 0
    end = len(s)-offset

    while s[start] == " ":
        start+=1
    while s[end]  == " ":
        end -= 1
    if start > end:
        return 0
    return s[start:(end+offset)]

s = " ciao "
print(check_w(s))
