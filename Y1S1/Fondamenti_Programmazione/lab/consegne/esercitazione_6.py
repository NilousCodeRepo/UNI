# I numeri di Tribonacci sono come i numeri di Fibonacci, ma ogni numero è funzione dei tre numeri
# di Tribonacci precedenti (anziché solo dei due precedenti come in Fibonacci).
# Ad esempio, tribonacci(n) = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3).
# tribonacci(0) = tribonacci(1) = 0
# tribonacci(2) = 1
# Scrivere una funzione ricorsiva che dato n, restituisca l'n-esimo numero di Tribonacci
def tribonacci(n: int):
    pass


# Scrivere una funzione ricorsiva che data una lista di interi, restituisca il massimo
# Non usare cicli for/while
def max_recursive(l: List[int]) -> int:
    pass


# Scrivere una funzione ricorsive che calcola la somma dei numeri da 0 a n (incluso)
def sum_recursive(n: int) -> int:
    pass


# Scrivere una funzione ricorsiva che calcoli la potenza di un numero,
# utilizzando la seguente formula: power_recursive(base, exp) = base * power_recursive(b, exp-1)
# Non potete usare pow(...) o l'operatore **
def power_recursive(base: int, exp: int) -> int:
    pass


# Scrivere una funzione ricorsiva che prende in input una stringe e restituisce
# la stringa invertita (ad esempio, "ciao" - > "oaic").
# Le uniche operazioni su stringhe permesse sono la concatenazione fra stringhe e lo slicing.
def reverse_recursive(s: str) -> str:
    pass


# Scrivere una funzione ricorsiva che controlla se un numero è un numero primo
# (controllando che non sia divisibile per tutti i numeri precedenti ad esso).
# La funzione prende in input il numero n da controllare, ed un divisore d (all'inizio d==2)
def is_prime_recursive(n: int, d=2) -> bool:
    pass


# La Torre di Hanoi (anche conosciuta come Torre di Lucas dal nome del suo inventore)
# è un rompicapo matematico composto da tre paletti e un certo numero di dischi di
# grandezza decrescente, che possono essere infilati in uno qualsiasi dei paletti.
# Il gioco inizia con tutti i dischi incolonnati su un paletto in ordine decrescente,
# in modo da formare un cono. Lo scopo del gioco è portare tutti i dischi su un paletto diverso,
# potendo spostare solo un disco alla volta e potendo mettere un disco solo su un altro disco più grande,
# mai su uno più piccolo.
# La soluzione base del gioco della torre di Hanoi si formula in modo ricorsivo.
#
# Siano i paletti etichettati con A, B e C, e i dischi numerati da 1 (il più piccolo) a n (il più grande).
# L’algoritmo si esprime come segue:
#
# Sposta i primi n-1 dischi da A a B. (Questo lascia il disco n da solo sul paletto A)
# Sposta il disco n da A a C
# Sposta n-1 dischi da B a C
#
# Scrivere una funziona che calcola il numero minimo di mosse necessarie per spostare
# gli n dischi da uno paletto all’altro.
def hanoi_moves(n: int) -> int:
    pass


# Nota: esercizio difficile
# Scrivere una funzione che risolve il problema dello zaino.
# Dato una lista di tuple l=[(w0, v0), (w1, v1), ...], dove wi è
# il peso in kg dell'oggetto i-esimo, e vi è il suo valore in euro,
# scrivere una funzione che prenda in input la lista l, e un peso massimo W.
# La funzione deve restituire la somma dei valori degli oggetti in una lista
# r=[(wk, vk), (wj, vj), ...] contenente un sottoinsieme delle tuple di input,
# tale che la somma dei pesi sia minore o uguale a W e il valore totale (in euro)
# sia il massimo possibile
def knapsack(l: List[Tuple[int, int]], W: int) -> int:
    pass
