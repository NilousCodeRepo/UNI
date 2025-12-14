#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from math import sqrt
from tree import BinaryTree
from nary_tree import NaryTree

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA
"""
nome       = "A"
cognome    = "S"
matricola  = "42"
################################################################################
################################################################################
################################################################################
# %% ----------------------------------- EX.1 ----------------------------------- #
"""
Ex1: 6 punti
Implementate la funzione ex1(N) che, dato un intero N positivo o nullo, 
restituisce l'N-esimo termine della successione di Lucas del primo tipo, U(N, P, Q), definita come segue:
    U(0, *, *) = 0
    U(1, *, *) = 1
    U(n, P, Q) = P * U(n-1, P, Q) - Q * U(n-2, P, Q) per n >= 2.

La funzione deve essere ricorsiva, oppure chiamare una funzione ricorsiva top-level, ossia definita esternamente 
ed al suo stesso livello nel file corrente. 
"""
def ex1(N, P, Q):
    pass
    # completa la funzione
    if N in [0,1]: 
        return N
    return P * ex1(N-1, P, Q) - Q * ex1(N-2, P, Q)

# %% ----------------------------------- EX.2 ----------------------------------- #
'''
Ex2: 8 punti

Implementa la funzione ex2(root) che riceve in ingresso root, un'istanza di albero binario, così come definito
nella classe BinaryTree del modulo tree. 
La funzione deve trovare e restituire il massimo valore che si ottiene, per ciascun nodo dell'albero,
calcolando la differenza in valore assoluto tra:
-   la somma dei valori dei nodi del sottoalbero sinistro
- e la somma dei valori dei nodi del sottoalbero destro 
Per un nodo foglia, la differenza è 0. 

La funzione deve essere ricorsiva, oppure chiamare una funzione ricorsiva top-level, ossia definita esternamente 
ed al suo stesso livello nel file corrente. 
'''

def somma(root):
    if root is None:
        return 0
    else:
        return somma(root.left) + somma(root.right) + root.value

def ex2(root: BinaryTree):
    pass
    # completa la funzione
    if root is None: 
        return 0
    diff = abs(somma(root.left) - somma(root.right))
    diff_SX = ex2(root.left)
    diff_DX = ex2(root.right)
    return max(diff, diff_SX, diff_DX)

# %% ----------------------------------- EX.3 ----------------------------------- #
'''
Ex3: 8 points 
Implementa la funzione ex3(dirin, K, extensions) che, dato il percorso di una directory dirin, 
un intero K e una lista di estensioni target (es. ['txt', 'pdf']), deve trovare tutte 
le directory che contengono un numero sufficiente di file con una delle estensioni specificate.

Restituisci un dizionario che ha:
  - Come chiavi: il path completo (stringa) di ogni directory (usando '/' come separatore).
  - Come valori: il numero totale di file (conteggiati ricorsivamente in tutti i sottolivelli) 
    la cui estensione è presente nella lista extensions.
Il dizionario deve includere solo le directory in cui il conteggio totale di tali file è strettamente maggiore di K.

La funzione deve essere ricorsiva, oppure chiamare una funzione ricorsiva top-level, ossia definita esternamente 
ed al suo stesso livello nel file corrente. 
'''

import os
def ex3(dirin, K, extensions):
    pass
    # completa la funzione
    D = esplora_directory(dirin,extensions)
    for path in list(D.keys()):
        if D[path] <= K:
            del D[path]
    return D

def esplora_directory(dirin, extensions):
    D = {dirin:0}
    for nome in os.listdir(dirin):
        fullname = dirin + '/' + nome
        if os.path.isdir(fullname):
            sottodir = esplora_directory(fullname, extensions)
            D[dirin] += sottodir[fullname]
            D.update(sottodir)
        else:
            for e in extensions:
                if nome.endswith(e):
                    D[dirin] += 1
    return D
    
    
# %% ----------------------------------- EX.4 ----------------------------------- #
'''
Ex4: 8 punti

Implementa la funzione ex4(root), ricorsiva o utilizzando funzioni ricorsive, 
che riceve l'argomento:  
    - root: la radice di un albero binario;
    
L'albero è composto da istanze della classe BinaryTree definita in tree.py. 
La funzione deve costruire e ritornare una lista, in mode che
ogni elemento alla posizione i-esima alla fine dovrà contenere la somma di tutti i nodi 
che si trovano alla profondità i (la radice dell'albero è alla profondità 0).

    Esempio:
                                                                        Profondità
        ______5______                        ______2______                   0
       |             |                      |             |
       8__        ___2___                __ 7__        ___5___               1
          |      |       |              |      |      |       |
          3      9       1             _4_     3_    _0_     _5_             2
                                      |   |      |  |   |   |   |
                                      2   -1     1  8   3   2   9            3

    Per l'albero di sinistra il risultato sarà [5, 10, 13]
    Per l'albero di destra   il risultato sarà [2, 12, 12, 24]
'''

from tree import BinaryTree

def ex4(root):
    pass
    # completa la funzione
    L = []
    esplora_albero(root, L, 0)
    return L

def esplora_albero(nodo, lista, profondità):
    if nodo is None: return
    if len(lista) <= profondità:
        lista.append(nodo.value)
    else:
        lista[profondità] += nodo.value
    esplora_albero(nodo.left,  lista, profondità+1)
    esplora_albero(nodo.right, lista, profondità+1)


######################################################################################

if __name__ == '__main__':
    # Puoi provare qui le tue implementazioni senza che interferiscano con il grader
    pass

