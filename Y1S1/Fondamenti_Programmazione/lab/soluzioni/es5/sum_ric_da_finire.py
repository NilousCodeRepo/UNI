# Scrivere una funzione ricorsive che calcola la somma dei numeri da 0 a n (incluso)
def sum_recursive(n: int) -> int:
    #caso base
    if n == 0:
        return 0
    m = n-1
    return sum_recursive(n) + sum_recursive(m)
