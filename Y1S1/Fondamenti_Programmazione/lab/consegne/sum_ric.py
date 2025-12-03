# Scrivere una funzione ricorsive che calcola la somma dei numeri da 0 a n (incluso)
def sum_recursive(n: int) -> int:
    #caso base
    if n == 0:
        return n
        
    S =  sum_recursive(n) + sum_recursive(n-1)
    
    return S

n = 10
print(sum_recursive(n))
