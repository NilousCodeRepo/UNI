# Implementare una funzionalità equivalente a `dict.update()`, che data una
# lista di dizionari, ritorna un dizionario con tutte le chiavi presenti nei
# dizionari di input. Per valori, si usano i valori nei dizionari di input
# scegliendo quelli dei dizionari con indice superiore se presenti.
def update_dict(dictionaries: List[dict]) -> dict:
    pass


# Implementare una funzione che prende in input una lista di dizionari e ritorna
# un dizionario le cui chiavi sono le chiavi presenti nei dizionari di input e come
# valori ritorna una lista con i valori presenti nei dizionari di input.
# Si possono usare i set.
def merge_dict(dictionaries: List[dict]) -> dict:
    pass


# Implementare una funzione che prende in input una lista di dizionari e ritorna
# un dizionario le cui chiavi sono quelle presenti in tutti i dizionari e i cui
# valori sono la lista di valori delle relative chiavi. Si possono usare i set.
def intersect_dict(dictionaries: List[dict]) -> dict:
    pass


# Scrivere una funzione che data una stringa, ritorna una lista di tuple
# consituita da parola e frequenza, ordinata per frequenza. La frequenza è
# il numero di volte in cui la parole appare nel testo.
# Per evitare problemi nel trovare le parole, togliere tutti i caratteri
# non alfanumerici, a parte gli spazi, e convertire le parole in minuscolo.
# Usare la funzione `isalnum()` per testare i caratteri.
def word_frequency(string: str) -> List[Tuple[str, int]]:
    pass

# Scrivere una funzione che data una stringa di numeri interi separati da spazi,
# ritorna la lista ordinata dei numeri interi con frequenza massima.
def number_frequency(string: str) -> List[int]:
    pass


    

# Scrivere una funzione che restituisce True se una lista di interi
# è composta da una prima parte ordinata in modo crescente, seguita
# da una seconda parte ordinata in modo decrescente (o viceversa).
# Le due parti non devono avere necessariamente la stessa lunghezza.
# Utilizzare un solo ciclo e non utilizzare sorted/sort, ne la funzione
# is_sorted implementata precedentemente.
# Si assuma che la lista abbia almeno sempre 3 elementi.
def is_sorted_half(a: list) -> bool:
    pass
