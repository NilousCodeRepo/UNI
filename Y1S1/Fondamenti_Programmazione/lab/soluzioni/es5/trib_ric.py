# I numeri di Tribonacci sono come i numeri di Fibonacci, ma ogni numero è funzione dei tre numeri
# di Tribonacci precedenti (anziché solo dei due precedenti come in Fibonacci).
# Ad esempio, tribonacci(n) = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3).
# tribonacci(0) = tribonacci(1) = 0
# tribonacci(2) = 1

# Scrivere una funzione ricorsiva che dato n, restituisca l'n-esimo numero di Tribonacci
def tribonacci(n: int):
    #caso base
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
        
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

n = 10
print(tribonacci(n))
