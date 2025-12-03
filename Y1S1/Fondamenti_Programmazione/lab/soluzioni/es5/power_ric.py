def p(base: int, exp: int) -> int :
    if exp == 0:
        return 1
    elif exp ==1:
        return base
    else:
        return base*p(base,exp-1)
