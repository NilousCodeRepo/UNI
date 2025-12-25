#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame è necessario:
    - risolvere almeno 3 esercizi di tipo func AND;
    - risolvere almeno 1 esercizio di tipo ex (problema ricorsivo) AND;
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale è dato dalla somma dei punteggi degli esercizi risolti.

Attenzione! DEBUG=True nel grade.py per migliorare il debugging.
Per testare correttamente la ricorsione è, però, necessario DEBUG=False.

"""

nome       = "T"
cognome    = "C"
matricola  = "217464"


# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 punti

Si definisca la funzione func1(int_list, keys) che prende in ingresso una
lista 'int_list' e un set 'keys' contenenti interi. La funzione restituisce
un dizionario in cui le chiavi sono gli interi in keys e i valori sono
liste con gli interi presenti in int_list divisibili per l'intero della
chiave corrispondente.
Le liste sono ordinate in ordine decrescente.


Esempio: se int_list=[4, 6, 10, 13] e keys={2, 3, 5}
  l'invocazione di func1(int_list, keys) deve restituire il dizionario
  {2:[10, 6, 4], 3:[6], 5:[10]}
'''
def func1(int_list, keys):
#	D:dict = {}
#
#	for el in keys:
#		D.setdefault(el)
#
#	v = 0 
#	for key in D.keys():
#		value = sorted( [v for v in int_list if v % key == 0], reverse=True)
#		D[key] = value
#	
#	return D
	return {key: sorted([v for v in int_list if v % key == 0], reverse=True) 
					for key in keys
				 }
# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti

Si definisca la funzione func2(L0, L1) che:
- Riceve 2 liste L0 e L1.

La prima lista L0 contiene stringhe S0, S1, ... Sn-1
la seconda lista L1 contiene numeri interi positivi I0, I1, ... In-1.

La funzione restituisce una stringa ottenuta concatenando ogni stringa
Sj ripetuta Ij volte.

Ad esempio, se L0 = ['ab', 'o o'] e L1 = [2, 3] la funzione restituisce:
'ababo oo oo o'.
'''
def func2(L0, L1):
	result = ""
	for i in range(len(L1)):
		result += L0[i] * L1[i]
	
	return result

# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 2 punti

Si definisca una funzione func3(string_list1, string_list2) che:

- Restituisce una nuova lista di stringhe tale che la nuova lista
	è costituita da tutte quelle stringhe presenti in una delle due liste in 
	ingresso che contengono come una sottostringa almeno una stringa o un 
	inverso dell'altra lista.

La lista risultante deve essere ordinata per numero di caratteri
decrescente, in caso di parità, in ordine alfabetico.

Esempio: se string_list1=['shop', 'park', 'elichopter', 'cat', 'elephant'] e
            string_list2=['ark', 'contact', 'hop', 'mark']

         l'invocazione di func3(string_list1, string_list2) dovrà restituire
         la lista ['elichopter','contact','park', 'shop']
         Infatti:
             'elichopter' contiene 'hop',
             'contact' contiene l'inverso di 'cat'
             'park' contiene 'ark'
             'shop' contiene 'hop'

'''

def func3(string_list1, string_list2):#non funziona
	string_list3 = set()
	
	for s1 in string_list1:
		for s2 in string_list2:
			if (s1 in s2 or s2 in s1 or s1[::-1] in s2 or s2[::-1] in s1):
				string_list3.add(s2) 
		
	return sorted(string_list3, key = lambda x: (-len(x), x) ) 

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 4 punti

Si definisca la funzione func4(D) che:

- Riceve in ingresso un dizionario, in cui ogni chiave è una stringa e il valore
corrispondente è un contenitore 

La funzione restituisce:

- Un elenco di liste, in cui ogni sottoelenco S 
	corrisponde a un elemento del dizionario in ingresso e contiene quanto
	segue:
		- Come primo elemento I0, la chiave dell'elemento del
			dizionario corrispondente 
		
		- Come secondo elemento I1, il valore dell'elemento del dizionario corrispondente.

Le liste interne sono ordinate in base alla lunghezza del secondo
elemento I1 in ogni lista interna, in ordine inverso (dalla più lunga
alla più corta).  

Se le due liste interne hanno un secondo elemento
con la stessa lunghezza, vengono ordinati in base al valore del primo
elemento I0 (in ordine alfabetico o numerico).

Ad esempio, se D = {"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}
la funzione restituisce: [["f", (1, 2, 3)], ["a", ["h", "w"]], ["c", {"f":3, "g":[1,2]}]].
"""

def func4(D):


D = {"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}
print(func4(D))

# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 punti

Si definisca una funzione func5(input_pngfile) che prende in ingresso
una stringa che contiene il percorso ad un file con un'immagine in
formato PNG.
L'immagine indicata da 'input_pngfile' contiene dei segmenti
orizzontali di colore uniforme su uno sfondo nero. Su una riga ci
possono essere più segmenti di colore diverso, anche attaccati fra
loro.

La funzione deve individuare tutti i segmenti presenti nell'immagine e
ritornare un lista di triple rappresentanti i colori dei segmenti
individuati, ordinati dal più lungo al più corto. In caso di segmenti
di uguale lunghezza, i colori vanno ordinati (in ordine crescente)
considerando l'ordine prima della terza componente, poi della seconda
e infine della prima.  In caso di segmenti di uguale colore, si deve
considerare quello con la lunghezza maggiore.

Esempio: nell'immagine del file func5/image01.png sono presenti quattro segmenti
         uno di lunghezza 50 con colore (0, 128, 200)
         uno di lunghezza 30 con colore (200, 128, 200)
         uno di lunghezza 30 con colore (200, 200, 128)
         uno di lunghezza 29 con colore (0, 128, 200),
         per cui func5('func5/image01.png') deve restituire la lista
         [(0, 128, 200), (200, 200, 128), (200, 128, 200)]
"""
import images

def func5(input_pngfile):
    # INSERT HERE YOUR CODE
    pass

# print(func5('func5/image01.png'))
# print(func5('func5/image02.png'))
# print(func5('func5/image03.png'))
# print(func5('func5/image04.png'))


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 8 punti

Si definisca la funzione ex1(L), ricorsiva o che utilizza funzioni o
metodi ricorsivi,che, data una lista di N liste di M caratteri
ciascuna, costruisce e restituisce la lista di tutte le possibili
stringhe di N caratteri ottenute concatenando un carattere della prima
lista, un altro della seconda, uno della terza e così via.

Ad esempio, se la lista di input è: [['c', 'q', 'a'], ['w', 'e', 'y']],
la funzione restituisce: ['ae', 'aw', 'ay', 'ce', 'cw', 'cy', 'qe', 'qw', 'qy'].
La lista ritornata deve essere ordinata in ordine alfabetico.

"""

def ex1(L):
    ## Scrivi qui il tuo codice
    pass

# L = [['c', 'q', 'a'], ['w', 'e', 'y']]
# print(ex1(L))
# L = [['0', '1'], ['0', '1'], ['0', '1'], ['0', '1']]
# print(ex1(L))
# L = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]
# print(ex1(L))
# L = [['0', '1', '2'], ['a', 'b', 'c'], ['0', '1', '2'], ['x', 'y', 'z']]
# print(ex1(L))

# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 marks

Si definisca la funzione ex2(root), ricorsiva o che utilizza funzioni
o metodi ricorsivi, che prenda in input un albero binario e lo
modifichi (in-place) aggiungendo ricorsivamente a ogni nodo i valori
dei suoi nodi figli (se presenti).
La somma deve essere fatta dal basso verso l'alto, cioè le foglie
saranno aggiunte ai loro nodi genitori, e così via, fino a raggiungere
la radice.
La funzione restituisce una coppia che rappresenta il numero di valori
dispari e pari nell'albero originale.

Ad esempio, se l'albero di input è:

               1
              / \
             2   3
            /   / \
           4   5   6
              /
             7
L'albero modificato sarà:
               28
              /  \
             6    21
            /    / \
           4    12  6
               /
              7
e la funzione restituirà (4, 3).
"""

import tree

def ex2(root):
    ## Scrivi qui il tuo codice
    pass
