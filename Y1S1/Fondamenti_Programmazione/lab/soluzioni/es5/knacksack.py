def ks(l: list[tuple([int, int])], W: int) -> int:
    if len(l) == 0 or W == 0:
        return 0
    w,v = l[(len(l)-1)]

    if w > W:
        return ks(l[0:len(l)-1], W)
    else:
        return max( (v + ks(l[0: len(l)-1]) W-w) , ks(l[0:len(l)-1], W) )
