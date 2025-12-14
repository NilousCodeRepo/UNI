# Scrivere una funzione ricorsiva che data una lista di interi, restituisca il massimo
# Non usare cicli for/while
def max_recursive(l: list[int]) -> int:
    print(l)
    #caso base
    if len(l) == 1:
        return l[0]
    else:
        m = min(l)
        l.remove(m)
'''
return max(l[0],max_recursive(l[1:len(l)]))

'''        
    return max_recursive(l)#tolgo un elemento ogni volta

l: list = [2,4,5,3,1]
print(max_recursive(l))
