# Scrivere una funzione ricorsive che calcola la somma dei numeri da 0 a n (incluso)
def sum_recursive(n: int) -> int:
    #caso base
    if n == 0:
        return 0
    else:
        return n + sum_recursive(n-1)
        
n:int = 3
print(sum_recursive(n))
