def prime_prim(n:int, d = 2) -> int:
    if n==d:
        return True
    elif n==1:
        return False
    else:
        return (n % d != 0) and prime_prim(n,d+1)
