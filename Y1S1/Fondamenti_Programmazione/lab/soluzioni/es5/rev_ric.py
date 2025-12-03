def rev_ric() -> str:
    if len(s) == 1:
        return s
    else:
        return s[-1]+rev_ric(s[0:len(s)-1])
