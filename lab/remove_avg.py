# Scrivere una funzione che data una lista contenente valori >= 0, 
# crei una nuova lista contentente soltanto gli elementi della lista 
# originale tali che soddisfano la seguente proprietà:
#    lista[i] > 2*media(lista[0:i])
# (Il primo elemento non viene quindi mai inserito)

# Ad esempio, si consideri la lista [5, 3, 10, 0]
#  Il primo elemento è 5. Non viene inserito

#  Il secondo elemento è 3, e la media degli elementi nel range [0, 0] è 5.
	# Poichè 3 < 5*2, l'elemento non viene inserito nella nuova lista

#  Il terzo elemento è 10, e la media degli elementi nel range [0, 1] è 4.
	# Poichè 10 > 4*2, l'elemento viene inserito nella nuova lista

#  Il quarto elemento è 0, e la media degli elementi nel range [0, 2] è 6.
	# Poichè 0 < 6*2, l'elemento non viene inserito nella nuova lista
def remove_avg(a: list) -> list:
